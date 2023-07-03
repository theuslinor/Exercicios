from random import *

numeros, par, impar = [], [], []


def sorteio():
    for i in range(5):
        numeros.append(randint(0, 100))
    return numeros


print(f'Sorteando 5 valores da lista: {", ".join(map(str, sorteio()))}.')


def somaPar():
    for num in numeros:
        if num % 2 == 0:
            par.append(num)
        else:
            impar.append(num)
    return par


somaPar()
print(f'\nSomando os valores pares de {", ".join(map(str, par))}, temos {sum(par)}.')
print(f'\nSomando todo os valores impares {", ".join(map(str, impar))}, temos {sum(impar)}.')
