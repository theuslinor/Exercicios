from random import randint
aleatorio = 0
tupla = []
print('Os números gerados são: ', end='')
for i in range(0,5):
    aleatorio = randint(0, 100)
    tupla.append(aleatorio)
    print(f'{aleatorio}', end=' ')
print('\nMenor numero foi {}'.format(min(tupla)))
print('Maior numero foi {}'.format(max(tupla)))
