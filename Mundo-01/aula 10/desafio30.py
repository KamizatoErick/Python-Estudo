# Crie um programa que leia um número inteiro
# e mostre na tela se ele é PAR ou IMPAR

n = int(input('Digite um número: '))

if n > 0:
    if (n%2) == 0:
        print('O número {} é PAR.'.format(n))
    if (n%2) == 1:
        print('O número {} é IMPAR.'.format(n))
else:
    print('Digite um valor maior de 0.')
