# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cadas valor serão entregues.
# Obs: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1

c50 = c20 = c10 = c1 = 0
valorSacar = int(input('Qual valor você quer sacar? R$'))
while True:
    if valorSacar == 0:
        break
    if valorSacar >= 50:
        valorSacar -= 50
        c50 += 1
    elif valorSacar >= 20:
        valorSacar -= 20
        c20 += 1
    elif valorSacar >= 10:
        valorSacar -= 10
        c10 += 1
    elif valorSacar >= 1:
        valorSacar -= 1
        c1 += 1
if c50 > 0: print(f'Total de {c50} de R$50')
if c20 > 0: print(f'Total de {c20} de R$20' )
if c10 > 0: print(f'Total de {c10} de R$10')
if c10 > 0: print(f'Total de {c1} de R$1')