# Desenvolva um programa que pergunte a distância de uma viagem em KM.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagem de até 200Km
# e R$0,45 para viagens mais longas.

km = float(input('Digite a distância da viagem em Km: '))

if km <= 200:
    preco = km * 0.5
    print('O preço da passagem ficou R${}'.format(preco))
else:
    preco = km * 0.45
    print('O preço da passagem ficou R${}'.format(preco))