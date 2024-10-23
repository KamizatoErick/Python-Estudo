#Faça um programa que leia uma STRING de 0 a 9999 e mostre na tela cada um dos digitos separados.

numero = input(str('Digite um numero de 0 a 9999: '))

totalCaractere = len(numero)

if(totalCaractere>4):
    print('Por favor, digite de 0 a 9999 apenas. Obrigado :)')

if(totalCaractere==4):
    print('Unidade: {}'.format(numero[3]))
    print('Dezena: {}'.format(numero[2]))
    print('Centena: {}'.format(numero[1]))
    print('Milhar: {}'.format(numero[0]))

if(totalCaractere==3):
    print('Unidade: {}'.format(numero[2]))
    print('Dezena: {}'.format(numero[1]))
    print('Centena: {}'.format(numero[0]))

if(totalCaractere==2):
    print('Unidade: {}'.format(numero[1]))
    print('Dezena: {}'.format(numero[0]))

if(totalCaractere==1):
    print('Unidade: {}'.format(numero[0]))
