soma = cont = 0
while True:
    numero = int(input("Digite um número [999 para parar]: "))
    if numero == 999:
        break
    cont += 1
    soma += numero
print(f'A soma dos {cont} valores foi {soma}!')