# Escreva um programa que faça o computador "pensar" 
# em um número inteiro entre 0 e 5 e peça para usuário
# tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

nAleatorio = random.choice([0,1,2,3,4,5])

while True:
    numero = int(input('Pensei em um número de 0 a 5, tente descobrir: '))
    
    if numero == nAleatorio:
        print('Parabéns, você acertou :)')
        break
    else:
        print('Você errou, tente novamente :( \n')
