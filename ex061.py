print('-'*10, 'Gerador de PA', '-'*10)
n1 = int(input('Primeiro termo: '))
n2 = int(input('Razão: '))
num = 1
while num <= 10:
    if num < 10:
        print(n1, end=' → ')
    elif num == 10:
        print(n1, end='')
    num += 1
    n1 += n2
print(' Acabou.')