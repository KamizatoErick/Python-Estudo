n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2

print('Sua média foi {}'.format(m))

if m >= 6.0:
    print('Sua média foi boa!')
else:
    print('Sua média foi ruim!')