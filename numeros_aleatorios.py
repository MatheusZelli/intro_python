import random

# numeros aleatorios em python
numero = random.randint(0,10)
print('Numero diferente = {0}'.format(numero))

# forçar sempre um mesmo numero
random.seed(1)
num = random.randint(0,10)
print('Sempre mesmo numero = {0}'.format(num))

#metodo choice()
lista = [3,5,1]
numer = random.choice(lista)
print(numer)
