# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
# No final, mostre os 10 primeiros termos dessa progressão.

import time

n = int(input('Primeiro termo: '))
r = int(input('Razão: ')) # pula de quanto em quanto

a10 = n + (11 - 1) * r # formula para descobrir o 10° número

print('Começando do número {} e pulando de {} em {}...'.format(n,r,r))

time.sleep(1)

for c in range(n, a10, r):
    print('{}'.format(c), end=' ')