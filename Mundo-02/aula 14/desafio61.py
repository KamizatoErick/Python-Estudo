# Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando estrutura while.

import time

n = int(input('Primeiro termo: '))
r = int(input('Razão: ')) # pula de quanto em quanto

a10 = n + (11 - 1) * r # formula para descobrir o 10° número

print('Começando do número {} e pulando de {} em {}...'.format(n,r,r))

time.sleep(1)

while n < a10:
    print(n, end=' ')
    n += r
   