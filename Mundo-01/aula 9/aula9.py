#Trabalhando com strings

frase = 'Curso em Video Python'
print('\n')

#Fatiamento
# [x:y:z]
# x começo, y final, z pula caracteres 

print(frase[2])
print(frase[2:13]) # 2 até o 13, excluindo o 13
print(frase[9:21]) #imprime 'Video Python'
print(frase[9:21:2]) #pulando de 2 em 2
print(frase[:5]) # caracter 0 até 4
print(frase[15:]) # indicando o início mas não indicando o final
print(frase[9::3])
print('-'*13)

#Análise
print(len(frase)) # mostra total de caracteres
print(frase.count('o')) # conta quantas vezes aparece a letra 'o'
print(frase.count('o',0,13)) # conta com fatiamento 0 até 13, excluindo o 13
print(frase.find('deo')) # quantas vezes encontrou 'deo', exibe a posição que começou
print(frase.find('Android')) # quando a frase não existir, retorna -1

if('Curso' in frase): #verifica se existe a palavra 'Curso' na frase
    print('Existe')

