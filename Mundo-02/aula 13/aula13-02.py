# Aprendendo laços: Passando início, fim e passo

num = int(input('Digite um número: '))

for c in range(0,num+1): # conta de 0 até num
    print(c)

i = int(input('Digite o início: '))
f = int(input('Digite o fim: '))
p = int(input('Digite o passo: '))

for c in range(i, f+1, p): # começa, termina e pula conforme o usuário digitou
    print(c)