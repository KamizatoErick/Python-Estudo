# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final mostre quantas pessoas ainda não atingiram 
# a maioridade e quantas já são maiores.

import datetime

# Variáveis
anoAtual = datetime.date.today().year # Pega o ano atual configurado na máquina
maiorIdade = 0
menorIdade = 0

for c in range(0,7):
    dataNascimento = int(input('Ano de nascimento da {}° pessoa: '.format(c+1)))

    if anoAtual-dataNascimento >= 18:
        maiorIdade += 1
    else:
        menorIdade += 1

print('\nExistem {} pessoas maior de idade.'.format(maiorIdade))
print('Existem {} pessoas menor de idade.'.format(menorIdade))

