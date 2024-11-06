s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')

nome = 'Erick'
idade = 24
salario = 1200.4
print(f'O {nome} tem {idade} anos e ganha R${salario:.2f}')