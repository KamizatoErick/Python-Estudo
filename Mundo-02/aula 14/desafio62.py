# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar 0 termos.

import time

n = int(input('Primeiro termo: '))
r = int(input('Razão: ')) # pula de quanto em quanto

a10 = n + (11 - 1) * r # formula para descobrir o 10° número

print('Começando do número {} e pulando de {} em {}...'.format(n,r,r))

while n < a10:
    print(n, end=' ')
    n += r

while True:
    novoTermo = int((input('\n\nDigite quantos termos a mais quer: ')))
    if novoTermo > 0:
        maisTermos = n + (novoTermo) * r
        print('\nMostrando mais {} termos:'.format(novoTermo))
        while n < maisTermos:
            print(n, end=' ')
            n += r
    else:
        break
print('Volte sempre :)')