a = (2,5,4)
b = (5,8,1,2)
c = a + b # (2,5,4,5,8,1,2)

print(len(c)) # mostra quantos tem dentro de 5

print(c.count(5)) # quantas vezes o 5 aparece em c
print(c)
print(c.index(5)) # em que posição está o primeiro 5
print(c.index(5,1)) # em que posição está o 5, começando da posição 1

pessoa = ('Erick',24,'M',65.5)
print(pessoa)
del(pessoa) # apaga a tupla