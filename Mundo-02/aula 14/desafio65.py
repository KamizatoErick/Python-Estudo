# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores
# e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar
# a digitar valores.

n = s = c = 0

while True:
    n = int(input('Digite um numero: '))
    s += n

# Confere maior e menor
    if c == 0:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    c += 1

    sair = str(input('Deseja digitar mais números? [S/N]: ')).upper()
    if sair == 'N' or sair == 'S':
        if sair == 'N':
            s = s/c
            print('\nA Média entre todos os números é {}'.format(s))
            print('O maior número foi o {}'.format(maior))
            print('O menor número foi o {}'.format(menor))
            break
    else:
        print('Opção inexistente.')
        break

