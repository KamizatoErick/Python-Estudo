# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

km = int(input('Digite a velocidade Km/h: '))
valorMulta = (km - 80) * 7.00

if km > 80:
    print('Você foi multado!')
    print('Você está a {}km/h acima do limite 80km/h.'.format(km-80))
    print('O valor da multa é R${}'.format(valorMulta))
else:
    print('Você não foi multado!')
    print('Continue assim :)')