listaNum = []
maiorpos = []
menorpos = []
for num in range(0, 5):
    listaNum.append(int(input('Digite um valor: ')))

menorValor = min(listaNum)
maiorValor = max(listaNum)

for i in range(len(listaNum)):
    if listaNum[i] == menorValor:
        menorpos.append(i+1)
    if listaNum[i] == maiorValor:
        maiorpos.append(i+1)

print('O maior valor é {} e está na posição {}.'.format(maiorValor, ', '.join(map(str, maiorpos))))
print('O menor valor é {} e está na posição {}.'.format(menorValor, ', '.join(map(str, menorpos))))