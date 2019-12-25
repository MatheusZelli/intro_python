# -*- coding: utf-8 -*-

num1 = float(input("Digite o primeiro número: "))
operador = input("Digite o operador: ")
num2 = float(input("Digite o segundo número: "))

#soma +
if operador == "+":
	resultado = num1 + num2
#subtração -
elif operador == "-":
	resultado = num1 - num2
#multiplicação *
elif operador == "*":
	resultado = num1 * num2
#divisão / 
elif operador == "/":
	resultado = num1 / num2
else :
	resultado = 'Operador inválido'

print(resultado)