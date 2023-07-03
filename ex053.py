'''frase = str(input('Digite uma frase: ')).replace(' ' and ',' and '.', '').upper()
print('O inverso de {} é {}'.format(frase, frase[::-1]))
if frase == frase[::-1]:
    print('\033[32mEsta frase é um Palíndromo!')
else:
    print('\033[31mEstá frase não é um Palíndromo!')'''
frase = str(input('Digite uma frase: ')).replace(' ' and ',' and '.', '').upper().split()
junto = ''.join(frase)
inverso = ''
for c in range(len(junto)-1, -1, -1):
        inverso += junto[c]
print(junto, inverso)