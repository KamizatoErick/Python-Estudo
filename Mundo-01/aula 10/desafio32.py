# Faça um programa que leia um ano qualquer e mostre se ele é Bissexto

ano = int(input('Digite um ano: '))

if (ano % 4) == 0:
    print('{} é um ano Bissexto!'.format(ano))
else:
    print('{} não é um ano Bissexto!'.format(ano))