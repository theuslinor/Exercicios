'''print('-' * 30)
print('{:^30}'.format('BANCO DA BAHIA'))
print('-' * 30)
saque = int(input('Digite o valor de saque: '))
cem = int(saque / 100)
saque = saque - (cem * 100)
cinquenta = int(saque / 50)
saque = saque - (cinquenta * 50)
vinte = int(saque / 20)
saque = saque - (vinte * 20)
dez = int(saque / 10)
saque = saque - (dez * 10)
cinco = int(saque / 5)
saque = saque - (cinco * 5)
um = int(saque / 1)
saque = saque - (um * 1)
print(f'\033[31m{cem} notas de 100 \n'
f'\033[32m{cinquenta} notas de 50 \n'
f'\033[33m{vinte} notas de 20 \n'
f'\033[34m{dez} notas de 10 \n'
f'\033[35m{cinco} notas de 5 \n'
f'\033[36m{um} notas de 1\033[m')'''

valor = int(input('Valor de saque: '))
total = valor
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break