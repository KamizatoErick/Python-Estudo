# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa mostre:
# - A média de idade do grupo
# - Qual é o nome do homem mais velho
# - Quantas mulheres têm menos de 20 anos

nomes = []
idades = []
sexos = []
mIdade = 0

# Recebe dados
for c in range(0,4):
    nome = str(input('Digite o nome da {}° pessoa: '.format(c+1)))
    idade = int(input('Digite a idade do(a) {}: '.format(nome)))
    sexo = str(input('Digite o sexo do(a) {} (M/F): '.format(nome))).strip().upper()
    nomes.append(nome) 
    idades.append(idade)
    sexos.append(sexo)

# Calula média idade
for c in range(0,4):
    mIdade += idades[c]
mIdade = mIdade / 4

# Nome do homem mais velho
idadeMaisVelho = 0
for c in range(0,4):
    if sexos[c] == 'M' and idades[c] > idadeMaisVelho:
        idadeMaisVelho = idades[c]
        homemMaisVelho = nomes[c]

# Mulheres com menos de 20 anos
mulherMenos20 = 0
for c in range(0,4):
    if sexos[c] == 'F' and idades[c] < 20:
        mulherMenos20 += 1

# Prits
print('\nA idade média do grupo é {}'.format(mIdade))
print('O homem mais velho é o {}, com {} anos'.format(homemMaisVelho,idadeMaisVelho))
print('Existem {} mulheres com menos de 20 anos'.format(mulherMenos20))