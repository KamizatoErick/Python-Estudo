reais = float(input('Digite quantos reais você tem: R$'))

dolares = reais / 5.64

print('Com R${:.2f} você pode comprar ${:.2f} dolares'.format(reais, dolares))