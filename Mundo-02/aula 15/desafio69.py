# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o
# usuário quer ou não continuar. No final, mostre:
# - Quantas pessoas tem mais de 18 anos.
# - Quantos homens foram cadastrados.
# - Quantas mulheres tem menos de 20 anos.

print('\n')
maiorIdade = menorIdade = homem = mulher = 0
while True:
    print('---'*10)
    print('CADASTRE UMA PESSOA')
    print('---'*10)

    idade = int(input('Idade: '))
    while True:            
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if sexo == 'M':
            homem += 1
            if idade > 18:
                maiorIdade += 1
            break
        elif sexo == 'F':
            mulher += 1
            if idade > 18:
                maiorIdade += 1
            if idade < 20:
                menorIdade += 1
            break
    while True:
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if opcao == 'N':
            terminar = True
            break
        if opcao == 'S':
            terminar = False
            break
    if terminar == True:
        break

print('---'*3)
print('Fim')
print(f'Ao todo temos {maiorIdade} pessoas maiores de idade.')
print(f'Temos {homem} homens.')
print(f'Existem {menorIdade} mulheres com menos de 20 anos')