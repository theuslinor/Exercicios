import numpy
soma = cont = 0
continuar = ''
numeros = []
while continuar != 'N':
    num = int((input('Digite um número: ')))
    soma += num
    cont += 1
    numeros.append(num)
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()
num_org = numpy.sort(numeros)
print('Você digitou {} números e a média foi {:.2f}\nO maior valor foi {} e o menor foi {}'.format(cont, soma/cont, num_org[-1], num_org[0]))