# Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas
# C) Uma listagem com as pessoas mais leves

pessoas = []
dado = []
maiorPeso = []
menorPeso = []
totpessoas = 0

while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    pessoas.append(dado[:])
        
    if len(maiorPeso) == 0:
        maiorPeso.append(dado[:])
        menorPeso.append(dado[:])
    elif dado[1] > maiorPeso[0][1]:
        maiorPeso.clear()
        maiorPeso.append(dado[:])
    elif dado[1] == maiorPeso[0][1]:
        maiorPeso.append(dado[:])

    elif dado[1] < menorPeso[0][1]:
        menorPeso.clear()
        menorPeso.append(dado[:])
    elif dado[1] == menorPeso[0][1]:
        menorPeso.append(dado[:])

    dado.clear()
    totpessoas += 1

    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ').upper().strip()[0])
    if opcao == 'N':
        break

#Prints
print()
print(f'Ao todo, você cadastrou {totpessoas} pessoas.')

print(f'O maior peso foi {maiorPeso[0][1]}Kg. Peso de',end=':')
for p in maiorPeso:
    print(f' {p[0]}',end=';')

print(f'\nO menor peso foi {menorPeso[0][1]}Kg. Peso de',end=':')
for p in menorPeso:
    print(f' {p[0]}',end=';')