'''
Imprime valores de duas listas
concatenando suas respectivas
posições/índices
'''

lista1 = [1,2,3]
lista2 = ['Matheus','Gabriel','Zelli']

for numero, nome in zip(lista1,lista2):
	print(numero,nome)