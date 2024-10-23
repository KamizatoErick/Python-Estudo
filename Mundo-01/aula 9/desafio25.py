# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.

nome = input('Digite seu nome completo: ')
nome = nome.upper()

if('SILVA' in nome):
    print('No seu nome tem "Silva".')
else:
    print('No seu nome não tem "Silva".')
