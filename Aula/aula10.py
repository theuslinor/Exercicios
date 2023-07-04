n1 = float(input('Qual sua primeira nota? '))
n2 = float(input('Qual sua segunda nota? '))
m = (n1+n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 10.0:
    print('Parabens, sua nota foi a maxima!')
elif m >= 9.0:
    print('Sua nota foi excelente!')
elif m >= 8.0:
    print('Sua nota foi muito boa, mas dá pra melhorar!')
elif m >= 7.0:
    print('Sua anota foi boa! melhore')
elif m >= 6.0:
    print('Sua nota foi minima pra passar, estude mais!')
else:
    print('Sua nota foi pésssima, melhore!')