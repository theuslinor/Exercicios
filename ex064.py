soma = cont = num = 0
while num != 999:
    num = int((input('Digite um número [999 para parar]: ')))
    if num < 999:
        soma += num
        cont += 1
    if num >= 999:
        break
print('Você digitou \033[32m{}\033[m números e a soma entre eles foi \033[35m{}\033[m\033[m.'.format(cont, soma))