num = [2, 5, 9, 1]
num [2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 5')
num.remove(2)
print(num)
print(f'Essa lista tem {len(num)} elementos.')



valores = list()
valores.append(5)
valores.append(9)
valores.append(1)
print(valores)



valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c + 1} encotrei o valor {v}')

a = [1, 2, 3, 5, 6]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
