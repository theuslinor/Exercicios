nu = int(input('digite um número para saber a tabuada dele: '))
cores = {'vermelho': '\033[31m', 'verde': '\033[32m', 'amarelo': '\033[33m', 'azul': '\033[34m', 'lilas': '\033[35m', 'azulclaro': '\033[36m', 'cinza': '\033[37m', 'limpa': '\033[m'}
n1 = nu * 1
n2 = nu * 2
n3 = nu * 3
n4 = nu * 4
n5 = nu * 5
n6 = nu * 6
n7 = nu * 7
n8 = nu * 8
n9 = nu * 9
n10 = nu * 10
print('A tabuada do {}{}{} é: \n {}{}{} x 1 = {} \n {}{}{} x 2 = {} \n {}{}{} x 3 = {} \n {}{}{} x 4 = {} \n {}{}{} x 5 = {} \n {}{}{} x 6 = {} \n {}{}{} x 7 = {} \n {}{}{} x 8 = {} \n {}{}{} x 9 = {} \n {}{}{} x 10 = {}' .format(cores ['vermelho'],nu,cores['limpa'],cores ['vermelho'], nu, cores ['limpa'], n1 , cores ['vermelho'],nu, cores ['limpa'], n2,cores ['vermelho'], nu, cores ['limpa'], n3,cores ['vermelho'], nu, cores ['limpa'] , n4, cores ['vermelho'],nu, cores ['limpa'], n5, cores ['vermelho'],nu,cores ['limpa'], n6, cores ['vermelho'],nu, cores ['limpa'], n7, cores ['vermelho'],nu, cores ['limpa'], n8,cores ['vermelho'], nu, cores ['limpa'], n9,cores ['vermelho'], nu,cores ['limpa'], n10))