import os
def clear_terminal():
    # Verifica o sistema operacional e executa o comando apropriado
    os.system('cls' if os.name == 'nt' else 'clear')
# Chama a função para limpar o terminal
clear_terminal()

#######################################################

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
elevado = n1 ** n2
divisaoInteira = n1 // n2
restoDivisao = n1 % n2

print("{} + {} = {}".format(n1, n2, soma))
print("{} - {} = {}".format(n1, n2, subtracao))
print("{} * {} = {}".format(n1, n2, multiplicacao))
print("{} / {} = {:.3f}".format(n1, n2, divisao)) #Trabalhando com 3 casas decimais no resultado
print("{} elevado a {} = {}".format(n1, n2, elevado))
print("{} // {} = {} (divisão inteira)".format(n1, n2, divisaoInteira))
print("{} %% {} = {} (resto da divisão)".format(n1, n2, restoDivisao))

