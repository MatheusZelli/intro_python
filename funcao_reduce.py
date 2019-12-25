'''
Recebe uma lista e retorna
um único valor

Útil para, por exemplo, soma de todos
os valores de uma lista
'''

from functools import reduce

def soma(x,y):
	return x+y

lista = [1,2,3,4,5]

soma = reduce(soma, lista)
print(soma)