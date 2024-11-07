lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim','Batata Frita')
# Tuplas são imutáveis

# Formas de visualizar
for comida in lanche:
    print(f'Eu vou comer {comida}')

print('-'*20)

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
    
print('-'*20)

for cont in range(0,len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('Comi pra caramba!')

print('-'*20)

# Sorted = Organizado
print(sorted(lanche))

