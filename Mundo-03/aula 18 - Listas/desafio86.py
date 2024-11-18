# Crie um programa que declare uma matriz de dimensão 3×3 
# e preencha com valores lidos pelo teclado. 
# No final, mostre a matriz na tela, com a formatação correta.

matriz = [[],[],[]]
dado = []

# Alimentação
for linha in range(0,3):
    for coluna in range(0,3):
        dado.append(int(input(f'Digite um valor para {[linha,coluna]}: ')))
        matriz[linha].append(dado[:])
        dado.clear()

print(20*'-=')

# Print Matriz
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'{matriz[linha][coluna]}',end='')
    print()
