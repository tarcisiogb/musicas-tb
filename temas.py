# -*- coding: utf-8 -*-
# ======================================================================
#  MAPA DE TEMAS DO SITE
# ----------------------------------------------------------------------
#  1) ORDEM_TEMAS: a ordem em que as secoes aparecem no site.
#  2) TEMA_DE: para cada musica (NOME DO ARQUIVO sem o .mp3), o tema dela.
#
#  PARA ADICIONAR UMA MUSICA NOVA:
#     - escreva uma linha em TEMA_DE, assim:   "NOME_DO_ARQUIVO": "Nome do Tema",
#     - se o tema ja existe, ela entra nele;
#     - se for um tema novo, coloque o nome tambem em ORDEM_TEMAS, na posicao que quiser.
#
#  Musica sem tema definido aqui cai sozinha na secao "A organizar" (no fim do site).
#  Depois de editar, rode:  python3 gerar_musicas.py
# ======================================================================

ORDEM_TEMAS = [
    "Luz e céu",
    "Horas do dia",
    "Estações e dias",
    "Domingos",
    "Pedras, cores e flores",
    "Texturas e ornamentos",
    "Formas e enigmas",
    "Mundo afora",
    "Inspirações",
    "Clássicos e homenagens",
    "Valsas",
    "Pista e groove",
    "Afetos e dedicatórias",
]

TEMA_DE = {
    # Luz e céu
    "ILUMINANDO": "Luz e céu",
    "LUMINA": "Luz e céu",
    "CINTILANTE": "Luz e céu",
    "REFLEXOS": "Luz e céu",
    "HEAVEN": "Luz e céu",
    "SUBLIME": "Luz e céu",
    "UNIVERSO": "Luz e céu",

    # Horas do dia
    "AMANHECER": "Horas do dia",
    "ORVALHO": "Horas do dia",
    "BRISA": "Horas do dia",
    "MADRUGADA": "Horas do dia",
    "PENUMBRA": "Horas do dia",
    "NOITE": "Horas do dia",
    "FANTASIA_CREPUSCULO": "Horas do dia",

    # Estações e dias
    "OUTONO": "Estações e dias",
    "VERAO": "Estações e dias",
    "SUMMER": "Estações e dias",
    "SUNNY": "Estações e dias",
    "PRINTEMPS": "Estações e dias",
    "SABADO": "Estações e dias",

    # Domingos (série)
    "DOMINGOSOLO": "Domingos",
    "DOMINGO_POP": "Domingos",
    "DOMINGO_BALAD16": "Domingos",

    # Pedras, cores e flores
    "JADE": "Pedras, cores e flores",
    "RUBI": "Pedras, cores e flores",
    "PEROLA": "Pedras, cores e flores",
    "AMBAR": "Pedras, cores e flores",
    "AZUL": "Pedras, cores e flores",
    "LILAS": "Pedras, cores e flores",
    "ORQUIDEAS": "Pedras, cores e flores",

    # Texturas e ornamentos
    "SEDA": "Texturas e ornamentos",
    "VELUDO": "Texturas e ornamentos",
    "FILIGRANA": "Texturas e ornamentos",
    "MOSAICO": "Texturas e ornamentos",
    "VINTAGE": "Texturas e ornamentos",

    # Formas e enigmas
    "ABSTRATO": "Formas e enigmas",
    "ENIGMA": "Formas e enigmas",
    "FRACTAIS": "Formas e enigmas",
    "LABIRINTO": "Formas e enigmas",

    # Mundo afora
    "ESPANOLA": "Mundo afora",
    "ARGENTINA": "Mundo afora",
    "LIBYA": "Mundo afora",
    "IBIZA_FAKE": "Mundo afora",
    "CIGANA": "Mundo afora",
    "COSITA": "Mundo afora",

    # Inspirações (série)
    "INSPIRAÇÃO_HOTEL_CALIF": "Inspirações",
    "INSPIRAÇÃO_SOUVENIR_DA_CHINA": "Inspirações",

    # Clássicos e homenagens
    "BACH": "Clássicos e homenagens",
    "MOZARIANA": "Clássicos e homenagens",
    "ADAGIO": "Clássicos e homenagens",
    "INTERMEZZO": "Clássicos e homenagens",
    "TANGATA": "Clássicos e homenagens",
    "SUITE_O_TEMPO_2021": "Clássicos e homenagens",
    "PIANO": "Clássicos e homenagens",
    "MAJESTOSA": "Clássicos e homenagens",

    # Valsas (série)
    "VALSA_MAIOR": "Valsas",
    "VALSINHA": "Valsas",

    # Pista e groove
    "BLUES": "Pista e groove",
    "GOLDEN_BLUES": "Pista e groove",
    "FUNKIEST_HOUSE": "Pista e groove",
    "MOVIE": "Pista e groove",
    "SOFT": "Pista e groove",
    "ACELERADA": "Pista e groove",

    # Afetos e dedicatórias
    "COMPANHEIRA": "Afetos e dedicatórias",
    "MEU_CANTINHO": "Afetos e dedicatórias",
    "DOCE_MEL": "Afetos e dedicatórias",
    "SEU_JUCA": "Afetos e dedicatórias",
    "VITORIA": "Afetos e dedicatórias",
    "LIBERTARIA": "Afetos e dedicatórias",
    "SUAVE": "Afetos e dedicatórias",

    # Ainda a definir (RAID, GO-NOGO, TOSW) — deixe de fora que vao para "A organizar",
    # ou escreva o tema aqui quando decidir.
}
