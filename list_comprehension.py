'''
Forma otimizada de criar uma nova
lista a partir de uma lista já existente
Sintaxe

y = [valor a adicionar - LAÇO REPETIÇÃO  - condicao]
'''

x = [1,2,3,4,5]

#quero adicionar numa nova lista
#os quadrados dos respectivos elementos
#da lista x

y = [i**2 for i in x]
print(y)

#quero adicionar apenas numeros ímpares
z = [i for i in x if i%2 == 1]
print(z)
