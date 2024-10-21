from random import choice

aluno1 = str(input('Primeiro aluno: '))
aluno2 = str(input('Segundo aluno: '))
aluno3 = str(input('Terceiro aluno: '))
aluno4 = str(input('Quarto aluno: '))

print('Sorteado: {}'.format(choice([aluno1, aluno2, aluno3, aluno4]))) #random.choice sorteia os nomes