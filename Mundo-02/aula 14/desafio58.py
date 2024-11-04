# Melhore o jogo do desafio 028 onde o computador vai "Pensar"
# em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final
# quantos palpites foram necessários para vencer.

import random

n = 1
p = 0
computador = random.randint(0,10)
print('-='*29)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-='*29)

while n != 0:    
    usuario = int(input('Em que número eu pensei? '))
    p += 1

    if computador == usuario:
        print('Você acertou. Foram {} palpites.'.format(p))
        n = 0
    else:
        print('Você errou, tente novamente...')