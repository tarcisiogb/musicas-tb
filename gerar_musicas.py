#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gera o musicas.js lendo os MP3 da pasta  musicas/  e casando cada um
com a capa (pasta capas/) e com o tema (arquivo temas.py).

>>> Cole em AUDIO_BASE a URL publica do seu bucket R2 (termina em .r2.dev/). <<<
    Enquanto vazia, os audios apontam para a pasta local.

Como usar:  python3 gerar_musicas.py
"""

import os, json
from urllib.parse import quote

# ----------------------------------------------------------------------
AUDIO_BASE = "https://pub-5fc5d1d8ff504c9faac869f244dd9d2f.r2.dev/"
# ----------------------------------------------------------------------

AUTOR = "Tarcísio Buzelin"
PASTA_MUSICAS = "musicas"
PASTA_CAPAS = "capas"
EXTS_CAPA = [".jpg", ".jpeg", ".webp", ".png"]
SEM_TEMA = "A organizar"

# carrega o mapa de temas (temas.py); se nao existir, tudo vai para "A organizar"
try:
    from temas import ORDEM_TEMAS, TEMA_DE
except Exception:
    ORDEM_TEMAS, TEMA_DE = [], {}


def titulo_do_arquivo(nome_base):
    t = nome_base.replace("_", " ").replace("-", " ")
    return " ".join(t.split()).title()


def achar_capa(nome_base, capas_disponiveis):
    por_stem = {}
    for arq in capas_disponiveis:
        stem, ext = os.path.splitext(arq)
        if stem.lower() == nome_base.lower():
            por_stem[ext.lower()] = arq
    for ext in EXTS_CAPA:
        if ext in por_stem:
            return por_stem[ext]
    return ""


def tema_do(nome_base):
    # busca sem diferenciar maiuscula/minuscula
    for chave, tema in TEMA_DE.items():
        if chave.lower() == nome_base.lower():
            return tema
    return SEM_TEMA


def url_audio(arquivo):
    caminho = "musicas/" + quote(arquivo)
    return (AUDIO_BASE + caminho) if AUDIO_BASE else caminho


def ordem_tema(tema):
    if tema == SEM_TEMA:
        return 100000               # "A organizar" sempre por ultimo
    if tema in ORDEM_TEMAS:
        return ORDEM_TEMAS.index(tema)
    return 999                       # tema fora da lista: antes de "A organizar"


def main():
    if not os.path.isdir(PASTA_MUSICAS):
        print("Nao encontrei a pasta '%s'." % PASTA_MUSICAS)
        return

    capas = os.listdir(PASTA_CAPAS) if os.path.isdir(PASTA_CAPAS) else []
    mp3s = [a for a in os.listdir(PASTA_MUSICAS) if a.lower().endswith(".mp3")]

    musicas = []
    com_capa = 0
    for arquivo in mp3s:
        base = os.path.splitext(arquivo)[0]
        capa_arq = achar_capa(base, capas)
        capa = ("capas/" + quote(capa_arq)) if capa_arq else ""
        if capa:
            com_capa += 1
        musicas.append({
            "titulo": titulo_do_arquivo(base),
            "autor": AUTOR,
            "tema": tema_do(base),
            "capa": capa,
            "audio": url_audio(arquivo),
            "dedicatoria": ""
        })

    # ordena por tema (na ordem definida) e, dentro do tema, por titulo
    musicas.sort(key=lambda m: (ordem_tema(m["tema"]), m["titulo"].lower()))

    corpo = json.dumps(musicas, ensure_ascii=False, indent=2)
    conteudo = (
        "// Gerado automaticamente por gerar_musicas.py\n"
        "// Titulos e dedicatorias podem ser editados aqui. Os temas ficam em temas.py.\n"
        "window.TEMAS_ORDEM = " + json.dumps(ORDEM_TEMAS, ensure_ascii=False) + ";\n"
        "window.MUSICAS = " + corpo + ";\n"
    )
    with open("musicas.js", "w", encoding="utf-8") as f:
        f.write(conteudo)

    # resumo por tema
    from collections import Counter
    cont = Counter(m["tema"] for m in musicas)
    destino = "R2" if AUDIO_BASE else "pasta local (GitHub)"
    print("Pronto! musicas.js com %d musica(s). Audios de: %s" % (len(musicas), destino))
    print("Com capa: %d  |  Sem capa: %d" % (com_capa, len(musicas) - com_capa))
    print("Por tema:")
    for tema in ORDEM_TEMAS + [SEM_TEMA]:
        if cont.get(tema):
            print("   - %s: %d" % (tema, cont[tema]))


if __name__ == "__main__":
    main()
