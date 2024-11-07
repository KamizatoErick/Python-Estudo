# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
# No final mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))
num = (n1,n2,n3,n4)

numero9 = num.count(9)
par = ()
primeiro3 = 0

# Põe o PAR na tupla 'par()'
for c in range(0,len(num)):
    if num[c] % 2 == 0:
        par += (num[(c)],0)
    if num[c] == 3:
        primeiro3 = num.index(3)

print(f'O número 9 apareceu {numero9} vezes')
if primeiro3>0: print(f'O primeiro número 3 está na posição {primeiro3+1}')
else: print('O número 3 não foi digitado')

print('Os valores pares digitados foram ',end='')
for c in range(0,len(par),2):
        print(par[c],end=' ')