# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# - A vista dinheiro/cheque: 10% de desconto
# - A vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

# Variáveis
valorProduto = float(input('Digite o valor do produto R$'))

print('=-'*20)
print('[0] - Dinheiro\n[1] - Cartão')
formaPagamento = int(input('Forma de pagamento: '))
print('=-'*20)

# Script
if formaPagamento == 0:
    valorDesconto = valorProduto - (valorProduto*0.10)
    print('\nVocê tem 10% de desconto, sendo R${:.2f} de desconto.'.format(valorProduto*0.10))
    print('De R${:.2f} para R${:.2f}'.format(valorProduto, valorDesconto))

elif formaPagamento == 1:
    parcela = int(input('Em quantas vezes? '))
    if parcela == 1:
        valorDesconto = valorProduto - (valorProduto*0.05)
        print('\nVocê tem 5% de desconto, sendo R${:.2f} de desconto.'.format(valorProduto*0.05))
        print('De R${:.2f} para R${:.2f}'.format(valorProduto, valorDesconto))
    elif parcela == 2:
        print('\nVocê não tem desconto.')
        print('O valor a pagar é R${:.2f}'.format(valorProduto))
    else:
        valorJuros = valorProduto + (valorProduto*0.20)
        print('\nVocê precisa pagar 20% de juros.')
        print('De R${:.2f} para R${:.2f}'.format(valorProduto, valorJuros))
        print('Por mês você pagará R${:.2f}'.format(valorJuros/parcela))

else:
    print('Não identifiquei essa forma de pagamento.')