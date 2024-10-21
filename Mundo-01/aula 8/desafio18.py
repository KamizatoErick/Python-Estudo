import math

angulo = float(input('Digite um angulo: '))

radiano = math.radians(angulo)

print('Seno {:.2f}'.format(math.sin(radiano)))
print('Cosseno {:.2f}'.format(math.cos(radiano)))
print('Tangente {:.2f}'.format(math.tan(radiano)))