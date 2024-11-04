# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

peso = []

# Lê os pesos
for c in range(0,5):
    pesoPessoa = float(input('Digite o peso da {}° pessoa: '.format(c+1)))
    peso.append(pesoPessoa)

# Variáveis
maior = 0
menor = peso[0]

# Verifica o maior peso
for c in range(0,5):
    if peso[c] > maior:
        maior = peso[c]
    
# Verifica o menor peso

for c in range(0,5):
    if peso[c] < menor:
        menor = peso[c]

print('O Maior peso é {}'.format(maior))
print('O Menor peso é {}'.format(menor))