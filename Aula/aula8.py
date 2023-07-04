n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2) / 2
print('Sua média foi {:.2f}'.format(m))
if m <= 4.9:
    print('Você foi reprovado! estuda mais')
elif m <= 5.9:
    print('Parabens você passou por pouco, estude mais!')
elif m <= 7.9:
    print('Parabéns, você foi bem!')
elif m <= 9.9:
    print('Você foi MUITO BEM! Parabéns!')
else:
    print('PARABENS! VOCÊ TIROU NOTA MAXIMA!!')