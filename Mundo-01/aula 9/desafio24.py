# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santos"

cidade = input(('Digite o nome de uma cidade: ')).strip()
dividido = cidade.split()

if('Santo' in dividido[0].capitalize()):
    print('"{}" começa com "Santo".'.format(cidade))
else:
    print('"{}" não começa com "Santo"'.format(cidade))