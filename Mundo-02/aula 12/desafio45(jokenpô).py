# Crie um programa que faça o computador jogar Jokenpô com você.

import os
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
import random
import time

# Cores
cores = {'limpa':'\033[m', 
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'amarelo':'\033[33m'}

# Variáveis
jokenpô = ['papel','tesoura','pedra']
computador = random.choice(jokenpô).upper()

# Script
while True:
    clear_terminal()
    computador = random.choice(jokenpô).upper()
    usuario = str(input('Pedra, Papel ou Tesoura? ')).upper()

    print('\nComputador: {}'.format(computador))
    print('Usuário: {}'.format(usuario))
    print('=-'*20)

    if computador == usuario:
        print('Empate, vamos novamente!'.format(computador))
        time.sleep(2)
    elif computador == 'PAPEL' and usuario == 'PEDRA':
        print('{}Computador: Hahaha, eu ganhei!{}'.format(cores['vermelho'],cores['limpa']))
        break
    elif computador == 'PEDRA' and usuario == 'TESOURA':
        print('{}Computador: Hahaha, eu ganhei!{}'.format(cores['vermelho'],cores['limpa']))
        break
    elif computador == 'TESOURA' and usuario == 'PAPEL':
        print('{}Computador: Hahaha, eu ganhei!{}'.format(cores['vermelho'],cores['limpa']))
        break
    else:
        print('{}Computador: Droga, eu perdi :({}'.format(cores['verde'],cores['limpa']))
        break