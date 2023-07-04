import modulos.uteis.numeros as nmr

numero = int(input('Digite o preço: '))
aumento = int(input('Valor do aumento: '))
decrecimo = int(input('Valor do decrécimo: '))

print(f'A metade de {nmr.moeda(numero)} é {nmr.moeda(nmr.metade(numero))}.')
print(f'O dobro de {nmr.moeda(numero)} é {nmr.moeda(nmr.dobro(numero))}.')
print(f'Aumentando {aumento}%, temos {nmr.moeda(nmr.aumentar(numero, aumento))}.')
print(f'Diminuindo {decrecimo}%, temos {nmr.moeda(nmr.diminuir(numero, decrecimo))}.')