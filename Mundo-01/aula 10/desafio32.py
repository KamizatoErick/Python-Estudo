# Faça um programa que leia um ano qualquer e mostre se ele é Bissexto
import datetime

ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))

if ano == 0:
    ano = datetime.date.today().year # Pega o ano atual configurado na máquina

if (ano % 4) == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é um ano Bissexto!'.format(ano))
else:
    print('{} não é um ano Bissexto!'.format(ano))