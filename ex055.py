pesomin = 0
pesomax = 0
for c in range(1, 4):
    peso = float(input('Digite o peso da {}º pessoa: '.format(c)))
    if c == 1:
        pesomax = pesomin = peso
    else:
        if peso > pesomax:
            pesomax = peso
        if peso < pesomin:
            pesomin = peso
print('O maior peso é {}kg'.format(pesomax))
print('O menor peso é {}kg'.format(pesomin))
