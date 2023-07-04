'''def lin():
    print('-' * 30)


lin()
print('Seu cu')
lin()
print('Aprenda Python')
lin()
print('Matheus')
lin()

def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)


titulo('Matheus')
titulo('Aprenda Python')
titulo('Seu cu')

def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B é {s}')


soma(b = 4, a = 5)
soma(5, 8)
soma(8, 19)

def contador(* num):
    print(num)

contador(2, 1, 5)
contador(8, 9)
contador(4, 4, 6, 3, 2)


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos +=1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)'''


def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)