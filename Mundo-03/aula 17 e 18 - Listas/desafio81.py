# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores ordenadas de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []

while True:
    lista.append(int(input('Digite um valor: ')))

    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? S/N ').upper().strip()[0])
    if opcao == 'N':
        break

print('=*'*20)

print(f'Você digitou {len(lista)} valores')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')

if 5 in lista:
    print('O valor 5 FAZ parte da lista!')
else:
    print('O valor 5 NÃO faz parte da lista!')