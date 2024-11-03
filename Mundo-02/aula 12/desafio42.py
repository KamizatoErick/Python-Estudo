# Refaça o DESAFIO 35 dos triangulos,
# acrescentando o recurso de mostrar que tipo de triangulo será formado:
# - Equilátero: Todos os lados iguais.
# - Isósceles: Dois lados iguais
# - Escaleno: Todos os lados diferentes

r1 = float(input('Digite o primeiro comprimento: '))
r2 = float(input('Digite o segundo comprimento: '))
r3 = float(input('Digite o terceiro comprimento: '))

if (r1+r2) > r3 and (r2+r3) > r1 and (r1+r3) > r2:
    print('É possível formar um triangulo!')
else:
    print('Não é possível formar um triangulo')

if r1 == r2 == r3:
    print('É Equilátero!')
elif r1 == r2 or r2 == r3 or r3 == r1:
    print('É Isósceles!')
else:
    print('É escaleno!')