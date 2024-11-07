# Crie um programa que tenha uma tupla totalmente preenchida
# com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20)
# e mostrá-lo por extenso.

extenso = ('zero','um','dois','três','quatro','cinco','seis','sete','oito',
           'nove','dez','onze','doze','treze','quatorze','quinze','dezesseis',
           'dezessete','dezoito','dezenove','vinte')
num = ''
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if (num >= 0) and (num <= 20):
        break

for c in range(0,21):
    if num == c:
        print(f'Você digitou o número {extenso[c]}!')
        break
        