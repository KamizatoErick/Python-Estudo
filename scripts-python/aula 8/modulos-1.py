#import math #importa a biblioteca inteira
from math import sqrt, ceil, floor #importa somente partes da biblioteca

num = int(input('Digite um numero: '))
raiz = sqrt(num)

print('A raiz de {} é igual a {}'.format(num, ceil(raiz))) #math.ceil arredonda para cima