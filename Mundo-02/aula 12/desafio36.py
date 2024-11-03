# Escreva um programa para aprovar o empréstimo bancário para comprar uma casa.
# O programa vai perguntar o valor a casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou
# então o empréstimo será negado.

# Cores
cores = {'limpa':'\033[m', 
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'amarelo':'\033[33m'}

# Variáveis
valorCasa = float(input('Qual é o valor da casa? R$'))
salario = float(input('Qual é o seu salário? R$'))
anos = float(input('Em quantos anos você vai pagar a casa? '))
valorMensal = valorCasa / (anos*12)

# Script
if valorMensal <= (salario * 0.30):
    print('\n{}Parabéns! O empréstimo foi aprovado :){}'.format(cores['verde'],cores['limpa']))
else:
    print('\n{}O valor do empréstimo foi reprovado :('.format(cores['vermelho']))
    print('O valor da parcela excede 30% do seu salário.{}'.format(cores['limpa']))

print(cores['amarelo'])
print('R${:.2f} parcela mensal.'.format(valorMensal))
print('30% do seu salário é R${:.2f}'.format(salario * 0.30))
print(cores['limpa'])