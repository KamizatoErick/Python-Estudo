# Crie um programa onde o usuário possa digitar sete valores numéricos
# e cadastre-os em uma lista única que mantenha separados os valores
# pares e ímpares. No final, mostre os valores e ímpares em ordem crescente.

numeros = [[],[]]
dado = []

for cont in range(1,8):
    dado.append(int(input(f'Digite o {cont}o. valor: ')))

    if dado[0] % 2 == 0:
        numeros[0].append(dado[0])
    else:
        numeros[1].append(dado[0])
    dado.clear()

numeros[0].sort()
numeros[1].sort()

print(f'Os valores pares digitados foram: {numeros[0]}')
print(f'Os valores impares digitados foram: {numeros[1]}')