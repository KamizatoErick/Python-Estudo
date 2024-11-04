# Crie um programa que leia dois valores
# e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa

# Explicação: Nesse programa eu comecei com a variável opcao 4, pois assim ele entra no laço pedindo 
# o n1 e n2. E caso o usuário opite por "[4] novo número", ele retorna  

opcao = 4

while opcao != 5:
# Recebe os dados e descobre maior
    if opcao == 4:
        n1 = int(input('\nDigite o 1° valor: '))
        n2 = int(input('Digite o 2° valor: '))
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        opcao = 0

# Menu
    if opcao == 0:
        print('''
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair''')    
        opcao = int(input('\nDigite a opção: '))

# Script opção
    if opcao == 1:
        print('{} + {} = {}'.format(n1,n2,n1+n2))
        opcao = 5
    elif opcao == 2:
        print('{} x {} = {}'.format(n1,n2,n1*n2))
        opcao = 5
    elif opcao == 3:
         print('Entre {} e {}, o maior é o {}'.format(n1,n2,maior))
         opcao = 5
    elif opcao == 4:
        print('\nDigite novos números')
        opcao = 4
    elif opcao == 5:
        opcao = 5
    else:
        print('Opção inválida.')
        opcao = 0
    
print('\nVolte sempre :)')