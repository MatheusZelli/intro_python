'''

'''
minha_lista = ["abacate","abacaxi","melancia"]
print(minha_lista)

#pode ser mista
minha_lista_2 = ["abacaxi",1,2,True,1.23]
print(minha_lista_2)

#posso printar uma posição específica usando o índice
#parte do índice 0 
print(minha_lista[2])

#posso printar usando FOR também
print("Usando o FOR")
for item in minha_lista:
	print(item)


#LEN para saber tamanho da lista
print("USANDO O LEN")
tamanho = len(minha_lista_2)
print(tamanho)

#inserir novo elemento na lista usando APPEND
print("usando APPEND")
minha_lista.append("limao")
print(minha_lista)

#SABER SE UM ELEMENTO EXISTE NA MINHA LISTA
print("Saber se elemento está na lista")
if True in minha_lista_2:
	print ("Tem verdade nessa lista")


#Para remover elementos de uma lista
print(minha_lista_2)
del minha_lista_2[2] #ou pode ser intervalo [2:4]
print (minha_lista_2)

#posso criar lista em branco
minha_lista_4 = [] #necessidade de adicionar aos poucos