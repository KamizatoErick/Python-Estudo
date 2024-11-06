# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar.
# No final, mostre:
# - Qual é o total gasto na compra
# - Quantos produtos custam mais de R$1000,00
# - Qual é o nome do produto mais barato
print('\n')
print('LOJA SUPER BARATÃO')
print('-'*20)

totalPreco = produtoMaiorMil = precoMenor = 0
while True:
    produto = str(input('Produto: ')).strip()
    preco = float(input('Preço: R$'))

    totalPreco += preco

    if preco > 1000:
        produtoMaiorMil += 1
    
    if preco < precoMenor or precoMenor == 0:
        precoMenor = preco
        produtoMenor = produto
    
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    
    if opcao == 'N':
      break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'Total gasto: R${totalPreco:.2f}')
print(f'Temos {produtoMaiorMil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {produtoMenor} que custa {precoMenor:.2f}')