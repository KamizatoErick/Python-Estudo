# Escreva um programa que faça o computador "pensar" 
# em um número inteiro entre 0 e 5 e peça para usuário
# tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
import time

nAleatorio = random.randint(1, 5) # Faz o computador "Pensar"

print('-='*29)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-='*29)

while True:
    numero = int(input('Em que número eu pensei? '))
    print('PROCESSANDO...\n')
    time.sleep(2)
    
    if numero == nAleatorio:
        print('Parabéns, você acertou :)')
        break
    else:
        print('Você errou, tente novamente :( \n')
