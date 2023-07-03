lista, listaPares, listaImpar, listaInt = [], [], [], []
numero = '0'
while numero.isdigit() == True:
    numero = (input('Digite um valor: '))
    lista.append(numero)
lista.pop()

for num in lista:
    listaInt.append(int(num))
lista = listaInt
lista.sort()

for num in lista:
    if num % 2 == 0:
        listaPares.append(num)
    else:
        listaImpar.append(num)
print('A lista é {}.'.format(', '.join(map(str, list(set(lista))))))
print('A lista de Impáres {}.'.format(', '.join(map(str, listaImpar))))
print('A lista de Pares {}'.format(', '.join(map(str, list(set(listaPares))))))
