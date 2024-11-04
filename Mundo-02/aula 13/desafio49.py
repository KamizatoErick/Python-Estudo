# Refaça o desafio 009, mostrando tabuada de um número 
# que o usuário escolher, só que agora utilizando um laço for.

num = int(input('Digite um número: '))
f = int(input('Digite até aonde quer a tabuada: '))

for c in range(1,f+1):
    print('{} x {} = {}'.format(num, c, num*c))