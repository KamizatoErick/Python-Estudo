# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas as letras minusculas
# Quantas letras ao todo (sem considerar os espaços)
# Quantas letrar tem o primeiro nome

nome = 'Erick Kamizato Scilo'

print(nome.upper())
print(nome.lower())

# Valida quantos espaços e quantos caracteres tem o nome
totalEspaco = nome.count(' ')
totalFrase = len(nome)
print('O nome tem {} letras, sem considerar os espaço'.format(totalFrase-totalEspaco))

dividido = nome.split()
print('O primeiro nome tem {} letras'.format(len(dividido[0])))