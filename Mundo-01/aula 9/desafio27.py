# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida:
# primeiro e o último nome separadamente.
# Exemplo: Ana Maria de Souza
# primeiro = Ana
# ultimo = Souza

nome = str(input('Digite seu nome: ')).strip()
nome = nome.split()
primeiroNome = nome[0]
ultimoNome = nome[len(nome)-1]

print(primeiroNome)
print(ultimoNome)
