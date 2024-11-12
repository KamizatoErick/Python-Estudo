# Este arquivo é somente para anotações sobre Listas

num = [2,5,9,1]
num[2] = 333
num.append(777)
num.sort() # ordem crescente
num.sort(reverse=True) # ordem decrescente
num.insert(2,555) # na posição 2, adiciona 555
print(num)

print(f'Essa lista em {len(num)} elementos')

num.pop() # remove o último
print(num)
num.pop(2) # remove o terceiro da fila
print(num)

num2 = [3,1,2,3,4,1]
if 1 in num2:
    num2.remove(1) # remove o primeiro elemento 1 (não varre até o final)
print(num2)

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f'{v}...')

for c,v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print('Cheguei ao final da lista.')

# Inserir valores na lista pelo teclado
valores2 = []
for cont in range(0,5):
    valores2.append(int(input('Digite um valor: ')))
print(valores2)

# Copia de lista
a = [1,2,3,4]
b = a[:] # Copia
b = a # Faz uma ligação entre as listas, o que eu mudar em B mudará em A