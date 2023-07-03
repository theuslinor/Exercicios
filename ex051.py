n1 = int(input('Primeiro termo: '))
n2 = int(input('Razão: '))
for n in range(n1, n2*10, n2):
    print('{} →'.format(n), end=' ')
print('ACABOU', end=' ')
