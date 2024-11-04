# Escreva um programa que leia um número n inteiro qualquer
# e mostre na tela os n primeiros elementos
# de uma Sequência de Fibonnaci.
# Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('{} -> {} '.format(t1,t2), end='')
c = 3
while c <= n:
    t3 = t1 + t2
    print('-> {} '.format(t3),end='')
    t1 = t2
    t2 = t3
    c += 1
print('-> FIM')