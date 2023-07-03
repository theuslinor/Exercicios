n = int(input('Digite um numero: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('o dobro de \033[31m{}\033[m é \033[32m{}\033[m, o triplo é \033[34m{}\033[m e a raíz quadrada é \033[35m{:.2f}\033[m' .format(n, d, t, r))