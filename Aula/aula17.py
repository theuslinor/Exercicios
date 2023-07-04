'''teste = []
teste.append('Matheus')
teste.append(23)
galera = []
galera.append(teste[:])
teste[0] = 'Vinicius'
teste[1] = 22
galera.append(teste[:])
print(galera)

#########################################################

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(p[0], p[1])'''

###################################

galera =[]
dado = []
totmaior = totmenor = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 18:
        print('{} é maior de idade.'.format(p[0]))
        totmaior += 1
    else:
        print('{} é menor de idade'.format(p[0]))
        totmenor += 1

print('Temos {} maiores e {} menores de idade.'.format(totmaior, totmenor))