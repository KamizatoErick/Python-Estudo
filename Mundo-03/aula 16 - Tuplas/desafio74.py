# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números, gerados e também indique o
# menor e o maior valor que estão na tupla.
from random import randint

num = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
print(f'Valores sorteados: {num}')

# Outra forma de descobrir maior e menor
# maior = 0
# for c in range(0, len(num)):
#     if num[c] > maior:
#         maior = num[c]
#     if c == 0:
#         menor = num[c]
#     if num[c] < menor:
#         menor = num[c]

print(f'O maior valor sorteado foi {max(num)}')
print(f'O menor valor sorteado foi {min(num)}')