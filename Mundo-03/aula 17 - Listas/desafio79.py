# Crie um programa onde o usuário possa digitar vários valores númericos e
# cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

valores = []

while True:
    valor = int(input('Digite um valor: '))
    
    if valor in valores:
        print('Valor duplicado! Não vou adicionar...')
    else:
        print('Valor adicionado com sucesso...')
        valores.append(valor)

    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ').upper().strip()[0])
    
    if opcao == 'N':
        break
    
valores.sort()
print(f'Você digitou os valores: {valores}')