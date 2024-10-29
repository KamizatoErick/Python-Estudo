# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.

nome = str(input('Digite seu nome completo: ')).strip()
nome = nome.upper()

if('SILVA' in nome):
    print('No seu nome tem "Silva".')
else:
    print('No seu nome não tem "Silva".')
