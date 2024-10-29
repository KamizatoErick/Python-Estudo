# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez

frase = str(input('Digite uma frase: ')).strip().upper()

print('A letra "a" aparece na frase {} vezes.'.format(frase.count('A')))
print('A letra "a" aparece primeira vez na posição {}'.format(frase.find('A')+1))
print('A última letra "a" aparece na posição {}'.format(frase.rfind('A')+1)) # procura a partir do lado direito
