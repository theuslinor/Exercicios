dig = int(input('Digite um número de 0 até 9999: '))
uni = dig % 10
dig = (dig - uni) / 10
dez = dig % 10
dig = (dig - dez) / 10
cen = dig % 10
dig = (dig - cen) / 10
mil = dig % 10
dig = (dig - mil) / 10
dez = int(dez)
cen = int(cen)
mil = int(mil)
print('''Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}'''.format(uni, dez, cen, mil, ))

'''num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('unidade {}. dezena {}. centena {}. unidade {}.' .format(u, d, c, u))'''