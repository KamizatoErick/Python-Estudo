# Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas
# C) Uma listagem com as pessoas mais leves

pessoas = []
dado = []
totPessoas = maiorPeso = menorPeso = cont = 0

while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    
    pessoas.append(dado[:])
    dado.clear()
    totPessoas += 1

    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ').strip().upper()[0])
    if opcao == 'N':
        break

# Total Pessoas
print()
print(f'Ao todo, você cadastrou {totPessoas} pessoas.')

# Maior Peso
print('O maior peso foi ',end='')
for p in pessoas:
    if p[1] > maiorPeso:
        maiorPeso = p[1]
print(f'{maiorPeso}Kg. Peso de',end='')
for p in pessoas:
    if maiorPeso == p[1]:
        print(f' {p[0]}',end=';')

# Menor Peso
print('\nO menor peso foi ',end='')
for p in pessoas:
    if cont == 0:
        menorPeso = p[1]
        cont += 1
    elif p[1] < menorPeso:
        menorPeso = p[1]
print(f'{menorPeso}Kg. Peso de',end='')
for p in pessoas:
    if menorPeso == p[1]:
        print(f' {p[0]}',end=';')