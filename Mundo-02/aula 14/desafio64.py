# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar '999'.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles.
# Desconsiderando '999'.

c = n = s = 0


while n != 999:
    n = int(input('Digite um número: '))
    if(n!=999):
        s += n
        c += 1
    else:
        n = 999

print('\nA soma de todos os números é {}'.format(s))
print('Você digitou {} números'.format(c))