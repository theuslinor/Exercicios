import math
n1 = float(input('Digite um numero: '))
n2 = float(input('Digite outro numero:'))
soma = (n1 * n1) + (n2 * n2)
raiz = math.sqrt(soma)
print('Comprimento do cateto oposto é de {}\nComprimento do cateto adjacente é {}\nA hipotenusa vai medir {:.2f}'.format(n1, n2, raiz))
