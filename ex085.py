lista = [[], []]
for i in range(1, 8):
    numero = int(input('Digite o {}º numero: '.format(i)))
    if numero % 2 == 0:
        lista[0].append(numero)
    else:
        lista[1].append(numero)
print('Os valores impares digitados foram: {}.'.format(', '.join(map(str, sorted(lista[0])))))
print('Os valores pares digitados foram: {}.'.format(', '.join(map(str, sorted(lista[1])))))


