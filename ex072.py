from time import sleep
numeros = 'zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze','catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
numero = int(input('Digite um número entre 0 e 20: '))

sleep(0.5)
while True:
    while True:
        if numero < 0 or numero > 20:
            numero = int(input('Numero incorreto, digite um número entre 0 e 20: '))
        else:
            break
    print(f'Você digitou o numero {numeros[numero]}.')
    sleep(0.5)
    continuar = str(input('Você quer continuar? [S/N]')).upper()[0]
    if continuar == 'N':
        break
    else:
        numero = int(input('Digite um número entre 0 e 20: '))
sleep(0.5)
print('Fim do Programa')