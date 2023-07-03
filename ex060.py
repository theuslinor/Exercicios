import numpy
numb = []
num = int(input('Digite um número: '))
for i in range (num, 1, -1):
    numb.append(i)
    print(i, 'x ', end='')
print('1 = {}'.format(numpy.prod(numb)))