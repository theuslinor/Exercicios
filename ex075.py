numeros = []
numeros_pares = []
for i in range(1,5):
    numero = int(input('Digite um número: '))
    numeros.append(numero)
    if numero % 2 == 0:
        numeros_pares.append(numero)
tupla_numero = tuple(numeros)
print('O valor 9 apareceu {} vezes.'.format(tupla_numero.count(9)))
if 3 in tupla_numero:
    print('O valor 3 apareceu na {}ª posição.'.format(tupla_numero.index(3)+1))
if numeros_pares:
    print('Os valores pares digitados foram: {}.'.format(', '.join(map(str, numeros_pares))))