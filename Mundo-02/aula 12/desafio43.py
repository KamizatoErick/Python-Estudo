# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# Calcule seu IMC e mostre seu status,
# de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do Peso.
# - Entre 18.6 e 24.9: Peso Ideal.
# - 25 até 29.9: Sobrepeso
# - 30 até 39.9: Obesidade
# - Acima de 40: Obesidade Mórbida

# Variáveis
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura**2)

# Script
if imc <= 18.5:
    print('Abaixo do Peso!')
elif imc >= 18.6 and imc <= 24.9:
    print('Peso Ideal!')
elif imc >= 25 and imc <= 29.9:
    print('Sobrepeso!')
elif imc >= 30 and imc <= 39.9:
    print('Obesidade!')
else:
    print('Obesidade Mórbida!')