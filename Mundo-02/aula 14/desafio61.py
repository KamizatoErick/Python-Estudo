# Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando estrutura while.

import time

n = int(input('Primeiro termo: '))
r = int(input('Razão: ')) # pula de quanto em quanto
termo = n
cont = 1
print('Começando do número {} e pulando de {} em {}...'.format(n,r,r))
time.sleep(1)

while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += r
    cont += 1
print('FIM')
   