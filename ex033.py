n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
n3 = int(input('Digite um numero: '))
if n1 > n2 and n1 > n3:
    print('{} é o numero maior'.format(n1))
elif n2 > n1 and n2 > n3:
    print('{} é o numero maior'.format(n2))
elif n3 > n1 and n3 > n2:
    print('{} é o numero maior'.format(n3))
if n3 > n1 and n2 > n1:
    print('{} é o numero menor'.format(n1))
elif n3 > n2 and n1 > n2:
    print('{} é o numero menor'.format(n2))
else:
    print('{} é o numero menor'.format(n3))

'''a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
menor = a
if b < a and b <c:
    menor = b
if c < a and c <b:
    menor = c
maior = a
if b > a and b >c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))'''
