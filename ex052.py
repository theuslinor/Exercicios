num = int(input('Digite um numero: '))
multi = 0
count = 0
while num <= 1:
    print('\033[31m{} não é numero primo\033[m'.format(num))
    num = int(input('Tente novamente: '))
print('\033[32m1\033[m', end=' ')
for c in range(2, num):
    if num % c == 0:
        count = count + 1
        multi = count + 1
        print('\033[32m{}\033[m'.format(c), end=' ')
    else:
            print('\033[31m{}\033[m'.format(c), end=' ')
    print('\033[32m{}\033[m'.format(num))
if multi != 0:
    print('\nO número \033[31m{}\033[m foi divisivel \033[32m{}\033[m vezes'
              '\nE por isso ele \033[31:4mNÃO É NUMERO PRIMO!\033[m'.format(num, multi + 1))
else:
    print('\nO número {} foi divisível \033[32m2\033[m vezes \n'
              'E por isso ele \033[32:4mÉ PRIMO\033[m.'.format(num))
