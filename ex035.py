4
r1 = float(input('Escreva um  número: '))
r2 = float(input('Escreva um  número: '))
r3 = float(input('Escreva um  número: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print('{:.2f}, {:.2f} e {:.2f} formam um TRIANGULO'.format(r1, r2, r3))
else:
    print('{:.2f}, {:.2f} e {:.2f} formam um TRIANGULO'.format(r1, r2, r3))