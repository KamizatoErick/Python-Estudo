# Crie um programa que leia dois valores
# e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa

import time
n1 = int(input('\nPrimeiro valor: '))
n2 = int(input('Segundo valor: '))

while True:
# Menu
    print('''
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair''')    
    opcao = int(input('\n>>>>> Digite a opção: '))

# Script opção
    if opcao == 1:
        print('{} + {} = {}'.format(n1,n2,n1+n2))
    elif opcao == 2:
        print('{} x {} = {}'.format(n1,n2,n1*n2))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {}, o maior é o {}'.format(n1,n2,maior))
    elif opcao == 4:
        print('\nInforme os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
        break
    else:
        print('Opção inválida.')
        opcao = 0
    print('---'*10)
    time.sleep(1.5)

print('\nVolte sempre :)')