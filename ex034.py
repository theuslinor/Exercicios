'''salario = float(input('Digite seu salário: '))
if salario <= 1250:
    aumento = salario + (15 * salario) / 100
    print('Seu salario de R${:.2f} foi aumentado para R${:.2f}, um aumento de 15%'.format(salario, aumento))
else:
    aumento = salario + (10 * salario) / 100
    print('Seu salario de R${:.2f} foi aumentado para R${:.2f}, um aumento de 10%'.format(salario, aumento))'''

salario = float(input('Digite seu salário: '))
aumento = 0
if salario <= 1250:
    aumento = salario * 0.15 + salario
    print(aumento)
else:
    aumento = salario * 0.10 + salario
    print(aumento)