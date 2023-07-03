from modulos.uteis.numeros import moeda, metade, aumentar, diminuir, dobro
numero = int(input('Digite o preço: '))
aumento = int(input('Valor do aumento: '))
decrecimo = int(input('Valor do decrécimo: '))

print(f'A metade de {moeda(numero)} é {moeda(metade(numero))}.\n'
      f'O dobro de {moeda(numero)} é {moeda(dobro(numero))}.\n'
      f'Aumentando {aumento}%, temos {moeda(aumentar(numero, aumento))}.\n'      
      f'Diminuindo {decrecimo}%, temos {moeda(diminuir(numero, decrecimo))}.')