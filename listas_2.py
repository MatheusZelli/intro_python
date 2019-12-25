lista = [2,401,145,47,67,99,4]

#ordena lista
lista.sort()

print(lista)

'''
Existe também a FUNÇÃO sorted(LISTA)
Exige que retorne conteúdo
Ou seja, quando uso ele, tenho que
atribuir conteudo a uma variável
'''
lista2 = [6,4,2,1]

lista2 = sorted(lista2)

print(lista2)

#Reverter uma lista

lista2.sort(reverse=True)
print(lista2)

#metodo reverse() - passa primeiro elemento p ultima posicao
# e assim sucessivamente

lista.reverse()
print(lista)

'''
Também ordena listas não numéricas
Strings, por exemplo, ordena alfabeticamente
'''
lista3 = ['Debora','Matheus','Ana','Beto']
lista3.sort()
print(lista3)