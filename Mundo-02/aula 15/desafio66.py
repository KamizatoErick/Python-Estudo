# Crie um programa que leia vários números inteiros.
# O programa só vai parar quando o usuário digitar o valor
# 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma
# entre eles (Desconsiderando 999).

cont = soma = 0

while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'A soma dos {cont} valores foi {soma}!')