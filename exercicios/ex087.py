matriz, pares = [], []
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f'Digite para [{i}, {j}]: '))
        linha.append(valor)
        if valor % 2 == 0:
            pares.append(valor)
    matriz.append(linha)
for linha in matriz:
    print('{:^5} {:^5} {:^5}'.format(*linha))

print('A soma dos valores pares é {}.'.format(sum(pares)))
print('A soma dos valores da terceira coluna é {}.'.format(matriz[0][2] + matriz[1][2] + matriz[2][2]))
print('O maior valor da segunda linha é {}.'.format(max(matriz[1])))