precoProduto = int(input('Digite o preço do seu produto: '))
desconto = int(input('Digite quantos porcentos de desconto deseja conceder ao produto: '))

descontoFormula = (precoProduto*(desconto/100))
precoDesconto = precoProduto - descontoFormula

print('\n')
print('O preço do produto é R${}'.format(precoProduto))
print('Desconto em valor R${}'.format(descontoFormula))
print('O novo preço será R${}'.format(precoDesconto))