# Leitor-de-Multiplos-Arquivos-de-Texto-em-Python

#-*- coding: utf-8 -*-

import os
#print("Arquivo .py está em:", os.path.abspath(__file__))
#print("Diretório atual de execução (CWD):", os.getcwd())

import os

PASTA = "documentos"

#print("Procurando em:", PASTA)
#print("Existe?", os.path.exists(PASTA))

for nome_arquivo in os.listdir(PASTA):
    caminho = os.path.join(PASTA, nome_arquivo)

    if caminho.endswith(".txt"):
        with open(caminho, "r", encoding="utf-8") as f:
            conteudo = f.read()
    
        print("=" * 40)
        print(f"Arquivo: {nome_arquivo}")
        print(conteudo)
