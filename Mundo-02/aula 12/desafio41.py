# A Confederação Nacional de Natação precisa de um programa 
# que leia o ano de nascimento de um atleta e mostre sua categoria, 
# de acordo com a idade:
# - Até 9 anos: Mirim
# - Até 14 anos: Infantil
# - Até 19 anos: Junior
# - Até 20 anos: Sênior
# - Acima: Master

import datetime

# Variáveis
anoAtual = datetime.date.today().year
idade = anoAtual - int(input('Digite o seu ano de nascimento: '))

# Script
if idade <= 9:
    categoria = 'Mirim'
elif idade > 9 and idade <= 14:
    categoria = 'Infantil'
elif idade > 14 and idade <= 19:
    categoria = 'Junior'
elif idade > 19 and idade <= 20:
    categoria = 'Sênior'
else:
    categoria = 'Master'

print('\nVocê tem {} anos, sua categoria é {}'.format(idade, categoria))