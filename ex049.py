numb = 0
tabuada = int(input('Digite um número: '))
for num in range(tabuada, tabuada * 11, tabuada):
    numb += 1
    print('{} x {} = {}'.format(tabuada, numb, num))
