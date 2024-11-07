# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
palavras = ('Aprender','programar','esquIlo','linguagem','python','curso','gratis','estudar',
            'futuro','mercado','trabalhar','erick','Omie','uoiea')
vogais = ('a','e','i','o','u')
for c in range(0,len(palavras)):
    print(f'\nNa palavra {palavras[c].upper()} temos ', end='')
    for vogal in range(0,len(vogais)):
            if vogais[vogal] in palavras[c].lower():
                    print(vogais[vogal],end= ' ')
