# Crie um programa que leia uma frase qualquer 
# e diga se ela é um palindromo, desconsiderando os espaços.
# Ex: APOS A SOPA
# Ex: A SACADA DA CASA
# Ex: A TORRE DA DERROTA
# Ex: O LOBO AMA O BOLO
# Ex: ANOTARAM A DATA DA MARATONA

frase = str(input('Digite uma frase: ')).replace(" ","")
tamanhoFrase = len(frase)

for c in range(0,tamanhoFrase):
    if frase[tamanhoFrase-1] == frase[c]:
        tamanhoFrase -= 1
        if c == tamanhoFrase:
            print('É um Palindromo')
    else:
        print('Não é um Palindromo')
        break