import math

cOposto = float(input('Digite o comprimento do cateto oposto: '))
cAdjacente = float(input('Digite o comprimento do cateto adjacente: '))

hipotenusa = (cOposto**2)+(cAdjacente**2)

print('O valor da hipotenusa é {:.2f}'.format(math.sqrt(hipotenusa))) #calculando na mão
print('O valor da hipotenusa é {:.2f}'.format(math.hypot(cOposto,cAdjacente))) #calculando usando o método hypot