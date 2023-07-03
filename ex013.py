salario = float(input('Qual é o seu salário atual? R$ '))
ajuste = salario + (15 * salario) / 100
print('Seu salário era de R${}, com reajuste de 15% seu novo salário é de R${}.'.format(salario, ajuste))