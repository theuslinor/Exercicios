import numpy
termo = int(input('Primeiro termo: '))
razao = int(input('Razão:'))
vezes = []
num = 1 
var = True
total_termos = 0 
while num <= 10:
    if num < 10:
        print(termo, end=' > ')
    else:
        print(termo, end=' > ')
    num += 1
    termo += razao
    total_termos += 1
print('cabou')
var = True
while var:
    escolha = int(input('\nQuantos termos você quer mostrar a mais? '))
    if escolha != 0:
        num = 1 
        while num <= escolha:
            print(termo, end=' > ')
            num += 1
            termo += razao
            mais = escolha
            total_termos += 1
        var = True
    else:
        var = False
print('Acabou, a razão foi usada {} vezes'.format(mais))
print('Total de termos exibidos:', total_termos)
