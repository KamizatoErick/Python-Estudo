# Desenvolva um programa que leia seis números inteiros e 
# mostre a soma apenas daquele que foram pares. 
# Se o valor digitado for impar, desconsidere-o.

# Bibliotecas
import time

# Variáveis
num = []
s = 0

# Laço para receber os seis números inteiros
for c in range(1,7):
    n = int(input('Digite o {}° valor: '.format(c)))
    num.append(n)

print('\n')

for c in range (0,6):
    if num[c] % 2 == 0:
        time.sleep(0.5)
        print('somando o numero {}...'.format(num[c]))
        s += num[c]

time.sleep(0.5)
print('O resultado final ficou {}'.format(s))