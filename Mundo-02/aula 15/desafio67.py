# Faça um programa que mostre a tabuada
# de vários números, um de cada vez,
# para cada valor digitado pelo usuário.
# O programa será interrompido quando
# o número solicitado for negativo.
while True:
    c = 1
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    while c <=10:
        print(f'{n} x {c} = {n*c}')
        c += 1
    print('-'*10)
print('Volte sempre :)')