# Faça um programa que leia 5 valores númericos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado
# e as suas respectivas posições na lista

lista = []

# Recebe os números
for cont in range(0,5):
    lista.append(int(input(f'Digite um valor para a posição {cont}: ')))

    if cont == 0:
        maior = menor = lista[cont]
    else:
        if lista[cont] > maior:
            maior = lista[cont]
        if lista[cont] < menor:
            menor = lista[cont]
        
# Prints
print('=*'*20)
print(f'Você digitou: {lista}')
print(f'O menor número digitado foi {menor} nas posições: ',end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}... ',end='')

print(f'\nO maior número digitado foi o {maior} nas posições: ',end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}... ',end='')