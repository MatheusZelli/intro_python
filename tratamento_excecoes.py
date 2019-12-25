a = 2
b = 0

'''
Defino num try o que se tenta executar, defino
uma mensagem para caso houver erro
'''
try:
	print(a/b)
except:
	print("Não é permitida a divisão por 0")

print(a/a)