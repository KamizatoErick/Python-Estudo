# Faça um programa que leia um número qualquer
# e mostre o seu fatorial.
# Exemplo: 5! = 5x4x3x2x1 = 120

num = int(input('Digite um valor: '))
c = num-1

print('Resolvendo {}!'.format(num))
while c != 0:
    num = num * c
    print('{:.0f} x {} = {}'.format(num/c,c,num))
    c -= 1
