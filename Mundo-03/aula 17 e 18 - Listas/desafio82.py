# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os
# valores pares e os valores impares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

lista = []

while True:
    lista.append(int(input('Digite um número: ')))

    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ').strip().upper()[0])
    if opcao == 'N':
        break

pares = []
impares = []

for v in lista:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
    
print('=*'*20)
print(f'Lista Completa: {lista}')
print(f'Lista dos Pares: {pares}')
print(f'Lista dos Impares: {impares}')