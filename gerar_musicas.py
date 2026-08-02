#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gera o arquivo musicas.js lendo os MP3 da pasta  musicas/  e casando
cada um com a capa de mesmo nome na pasta  capas/  (se existir).

Como usar (no Terminal, dentro da pasta do site):
    python3 gerar_musicas.py

Isso cria/atualiza o musicas.js com todas as musicas.
Depois voce pode abrir o musicas.js e ajustar os titulos que quiser.
Rode de novo sempre que adicionar musicas ou capas novas.
"""

import os, json

AUTOR = "Tarcisio Buzelin"          # autor fixo de todas as musicas
PASTA_MUSICAS = "musicas"
PASTA_CAPAS = "capas"
EXTS_CAPA = [".jpg", ".jpeg", ".png", ".webp"]


def titulo_do_arquivo(nome_base):
    # troca _ e - por espaco, junta espacos e deixa em Caixa de Titulo
    t = nome_base.replace("_", " ").replace("-", " ")
    t = " ".join(t.split())
    return t.title()


def achar_capa(nome_base, capas_disponiveis):
    # procura capas/<mesmo nome>.<ext>, sem diferenciar maiuscula/minuscula
    for arquivo in capas_disponiveis:
        stem, ext = os.path.splitext(arquivo)
        if stem.lower() == nome_base.lower() and ext.lower() in EXTS_CAPA:
            return PASTA_CAPAS + "/" + arquivo
    return ""


def main():
    if not os.path.isdir(PASTA_MUSICAS):
        print("Nao encontrei a pasta '%s'. Crie-a e coloque os MP3 dentro." % PASTA_MUSICAS)
        return

    capas = os.listdir(PASTA_CAPAS) if os.path.isdir(PASTA_CAPAS) else []

    mp3s = [a for a in os.listdir(PASTA_MUSICAS) if a.lower().endswith(".mp3")]
    mp3s.sort(key=lambda x: x.lower())

    musicas = []
    com_capa = 0
    for arquivo in mp3s:
        base = os.path.splitext(arquivo)[0]
        capa = achar_capa(base, capas)
        if capa:
            com_capa += 1
        musicas.append({
            "titulo": titulo_do_arquivo(base),
            "autor": AUTOR,
            "capa": capa,
            "audio": PASTA_MUSICAS + "/" + arquivo,
            "dedicatoria": ""
        })

    corpo = json.dumps(musicas, ensure_ascii=False, indent=2)
    conteudo = (
        "// Gerado automaticamente por gerar_musicas.py\n"
        "// Pode editar os titulos a vontade. Para escrever uma dedicatoria,\n"
        "// preencha o campo \"dedicatoria\" da musica desejada.\n"
        "window.MUSICAS = " + corpo + ";\n"
    )
    with open("musicas.js", "w", encoding="utf-8") as f:
        f.write(conteudo)

    print("Pronto! musicas.js gerado com %d musica(s)." % len(musicas))
    print("Com capa: %d  |  Sem capa (usando capa provisoria): %d" % (com_capa, len(musicas) - com_capa))


if __name__ == "__main__":
    main()
