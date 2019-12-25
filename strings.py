var1 = "Matheus"
var2 = " Gabriel"
var3 = "\n"

concatenar = var1 + var2 + var3


#FUNCAO STRIP - REMOVE ESPAÇOS E CARACTERES ESPECIAIS
print(concatenar.strip())

#lower e upper
print(concatenar.lower())
print(concatenar.upper())


#funcao slipt - converte STRING em uma lista,
#define-se o separador para isso

minha_string = "O Matheus é um rapaz muito charmoso"
minha_lista = minha_string.split(" ")
print(minha_lista)


#BUSCANDO SUBSTRINGS - FIND

minha_string = "O Matheus é um rapaz muito charmoso"

BUSCA = minha_string.find("rapaz")
print(BUSCA)
#PRINTANDO A PARTIR DE ONDE ENCONTROU "rapaz
print(minha_string[BUSCA:])

#quando não encontra substring retorna -1

#######################

#REPLACE - substitui partes de uma string

minha_string = minha_string.replace("Matheus","Paulo")

print("REPLACE = " + minha_string)