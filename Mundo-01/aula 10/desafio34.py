# Escreva um programa que pergunte o salário de um funcionário
# e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Inform o salario atual: R$'))

if salario > 1250.00:
    novoSalario = salario + (salario*0.10)

else:
    novoSalario = salario + (salario*0.15)

print('Quem ganhava {:.2f}, passa a ganhar R${:.2f}'.format(salario, novoSalario))