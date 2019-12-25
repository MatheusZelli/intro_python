
'''
Dicionários são listas de associações compostas por:
- uma chave
- um valor correspondente

Sintaxe:
dicionario = {'CHAVE':'valor'}
'''
dicionario_sites = {"Diego": "diegomariano.com"}

print(dicionario_sites['Diego'])

# dicionarios em python com varios elementos 
dicionario_sites = {"Diego": "diegomariano.com", "Google": "google.com", "Udemy": "udemy.com"}

print('Quando há varios elementos :')
for chave in dicionario_sites:
    print(dicionario_sites[chave])

#para imprimir chave especifica de um dicionario
print(dicionario_sites['Diego'])

'''
utilizar funcao items
'''
print('items : ')
for i in dicionario_sites.items():
	print(i)

#funcao values
print("values : ")
for i in dicionario_sites.values():
	print(i)

#funcao keys
print('keys : ')
for i in dicionario_sites.keys():
	print(i)