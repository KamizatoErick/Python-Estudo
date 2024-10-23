# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez

frase = input('Digite uma frase: ')
frase = frase.upper()

print('A letra "a" aparece na frase {} vezes.'.format(frase.count('A')))
print('A letra "a" aparece primeira vez na posição {}'.format(frase.find("A")))

# Falta fazer a última posição
