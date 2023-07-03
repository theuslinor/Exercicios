lista = []

for i in range(5):
    numero = int(input(f'Digite o {i+1} valor: '))
    for j in range(len(lista)):
        if numero < lista[j]:
            lista.insert(j, numero)
            print(f'Inserido na posição {j+1}')
            break
    else:
        lista.append(numero)
        print('Item adicionado a posição 5')
print(lista)