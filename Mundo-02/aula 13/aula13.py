# Aprendendo laços

num = int(input('Fale um número para a tabuada: '))

for c in range(1,11):
    print('{} x {} = {}'.format(num,c,num*c))

print('-'*10)

for c in range(10,0,-1): # invertido
    print('{} x {} = {}'.format(num,c,num*c))

print('-'*10) 

for c in range(1,11,2): # pulando de 2 em 2
    print('{} x {} = {}'.format(num,c,num*c))