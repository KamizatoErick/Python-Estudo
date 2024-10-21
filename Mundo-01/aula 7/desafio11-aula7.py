largura = int(input('Digite a largura da parede em metros: '))
altura = int(input('Digite a altura da parede em metros: '))

area = largura * altura

print('Você precisa de {} litros para pintar uma área de {} metros quadrados'.format(area/2, area))
