# a2 + bx + c
# -b +- (sqrt(b2-4ac))/2

from math import sqrt

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = pow(b,2) - 4*a*c
raiz_delta = sqrt(delta)

x1 = (-b + raiz_delta)/(2*a)
x2 = (-b - raiz_delta)/(2*a)

print('x1 = %f' %x1) # %f para float
print('x2 = %f' %x2) # %f para float