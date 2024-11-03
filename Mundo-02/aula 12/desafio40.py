# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: Reprovado
# - Média entre 5.0 e 6.9: Recuperação
# - Média 7.0 ou superior: Aprovado

# Cores
cores = {'limpa':'\033[m', 
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'amarelo':'\033[33m'}

# Variáveis
n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
m = (n1 + n2) / 2

# Script
print('\nSua média foi {}\n'.format(m))
if m < 5:
    print('{}Reprovado!{}'.format(cores['vermelho'],cores['limpa']))
elif m >= 5 and m < 7:
    print('{}Recuperação!{}'.format(cores['amarelo'],cores['limpa']))
else:
    print('{}Aprovado!{}'.format(cores['verde'],cores['limpa']))