r1 = float(input('Escreva um  número: '))
r2 = float(input('Escreva um  número: '))
r3 = float(input('Escreva um  número: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    if r1 == r2 == r3:
        print('{:.2f}, {:.2f} e {:.2f} formam um traingulo EQUILATERO'.format(r1, r2, r3))
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('{:.2f}, {:.2f} e {:.2f} formam um ISÓSCELES'.format(r1, r2, r3))
    elif r1 != r2 != r3 != r1:
        print('{:.2f}, {:.2f} e {:.2f} formam um ESCALENO'.format(r1, r2, r3))
else:
    print('Os numeros informados não formam um triangulo')