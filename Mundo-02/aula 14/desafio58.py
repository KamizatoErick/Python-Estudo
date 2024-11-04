# Melhore o jogo do desafio 028 onde o computador vai "Pensar"
# em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final
# quantos palpites foram necessários para vencer.

import random

acertou = False
palpites = 0
computador = random.randint(0,10)
print('-='*29)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-='*29)

while not acertou:    
    usuario = int(input('\nEm que número eu pensei? '))
    palpites += 1

    if computador == usuario:
        print('Você acertou. Foram {} palpites.'.format(palpites))
        acertou = True
    else:
        if usuario < computador:
            print('Errou... põe mais')
        else:
            print('Errou... põe menos')