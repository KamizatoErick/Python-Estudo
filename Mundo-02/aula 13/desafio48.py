# Faça um programa que calcule a soma
# entre todos os números ímpares que são
# múltiplis de três e que se encontram
# no intervalo de 1 até 500.

s = 0

for c in range(1,501):
    if c % 2 == 1:
        if (c % 3) == 0:
            s += c
print('A soma de todos os valores solicitados é {}'.format(s))