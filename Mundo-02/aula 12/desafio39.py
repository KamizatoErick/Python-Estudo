# Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento
# - Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

import datetime

# Cores
cores = {'limpa':'\033[m', 
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'amarelo':'\033[33m'}

# Variáveis
anoAtual = datetime.date.today().year # Pega o ano atual configurado na máquina
anoNascimento = int(input('Digite o seu ano de nascimento: '))
idade = anoAtual - anoNascimento

# Script
if idade >= 18:
    print('\n{}Já tem idade para se alistar!'.format(cores['amarelo']))
    alistou = str(input('Você já se alistou? s/n:{} '.format(cores['limpa'])))
    print('\n')
    if alistou == 's':
        print('{}Bom trabalho :){}'.format(cores['verde'],cores['limpa']))
    elif alistou == 'n':
        print('{}Você precisa se alistar!'.format(cores['vermelho']))
        print('Passaram {} ano(s).{}'.format(idade-18,cores['limpa']))
    else:
        print('{}Essa opção que digitou não existe.{}'.format(cores['vermelho'],cores['limpa']))
else:
    print('\n{}Ainda faltam {} ano(s) para você se alistar.{}'.format(cores['amarelo'],18-idade,cores['limpa']))