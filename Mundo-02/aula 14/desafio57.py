# Faça um programa que leia o sexo de uma pessoa,
# mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente,
# até ter um valor correto.

n = 1
while n != 0:
    sexo = str(input('Digite o seu sexo: ')).upper()
    if sexo == 'M' or sexo == 'F':
        n = 0
    else:
        print('Sexo inexistente, tente novamente.\n')

print('Obrigado.')