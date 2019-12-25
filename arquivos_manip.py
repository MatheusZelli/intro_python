# -*- coding: utf-8 -*-
'''FUNCAO open(nome,modo)
nome = nome do arquivo propriamente dito
são 6 modos:
r - somente leitura
w - escrita(caso o arquivo já exista, ele será apagado e um novo
arquivo vazio será criado)
a - leitura e escrita (adiciona o novo conteúdo ao fim do arquivo)
r+ - (leitura e escrita)
w+ - escrita (o modo w+, assim como o w, apaga o conteúdo anterior
do arquivo)
a+ - leitura e escrita (abre o arquivo para atualizacao)

DEFAULT  - modo r

FUNCOES LEITURA
read() - le arquivo inteiro
readline() - le uma linha
readlines() - le arquivo e o armazena em uma lista 
'''
arquivo = open("arquivo.txt")

texto_completo = arquivo.read()
print(texto_completo)
