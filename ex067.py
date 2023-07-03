import random as r 
cores = ['\033[31m','\033[32m''\033[33m','\033[34m','\033[35m','\033[36m','\033[37m']
num = 1
tab = int(input('Quer ver a tabuada de qual valor? '))
while True:
    print(r.choice(cores),f'{tab} x {num} = {tab*num}')
    num += 1
    if num == 11:
        num = 1
        tab = int(input('\033[mQuer ver a tabuada de qual valor? '))
        if tab < 0:
            break
        if num == 10:
            break
print('null')