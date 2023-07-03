import modulos.uteis.numeros as nmr
numero = int(input('Digite o preço: '))
aumento = int(input('Valor do aumento: '))
decrecimo = int(input('Valor do decrécimo: '))
print(f'A metade de R${numero} é R${nmr.metade(numero)}.')
print(f'O dobro de R${numero} é R${nmr.dobro(numero)}.')
print(f'Aumentando {aumento}%, temos R${nmr.aumentar(numero, aumento)}.')
print(f'Diminuindo {decrecimo}%, temos R${nmr.diminuir(numero, decrecimo)}.')