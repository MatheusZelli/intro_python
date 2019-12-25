# -*- coding: utf8 -*-
"""
Comandos condicionais

IF - executa um bloco SE uma determinada condição for atendida

"""

a = 5
b = 7

if a > b:
	print("A variável 'a' é maior")
else:
	print("A variável 'b' é maior")

# Indentação é muito importante no Python, pois a partir desse
# se define os blocos

# ELIF

x = 2
y = 1

if x==y:
	print("numeros iguais")
elif y>x:	
	print("Y maior \nque X")
else:
	print("Deu ruim")


#LAÇOS DE REPETIÇÃO ##########

#WHILE
x = 1

while x<10:
	print(x)
	x += 1


# LAÇO FOR

lista1 = [1,2,3,4,5]
lista2 = ["ola","mundo","!"]
lista3 = [0,"ola","biscoito","9.99",True]

for i in lista1:
	print(i)

for i in lista2:
	print(i)


## FOR E RANGE
for i in range(10):
	print(i)


for i in range(10,20,2): ##DO 10 AO 20 SENDO DOIS EM DOIS
	print(i)

	