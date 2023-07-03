palavras = ("Bicicleta", "Pistache", "Inverno", "Fantasma", "Rubi", "Misterio", "Leopardo", "Prazer", "Circo", "Aspirina", "Abacate", "Pimenta", "Girassol", "Veludo", "Estrada", "Pneu", "Cachorro", "Almofada", "Esmeralda", "Futebol")
print('A palavra: ', end='')
for palavra in palavras:
    letraVogais = []
    for letra in palavra:
        if letra.lower() in 'aeiou':
            letraVogais.append(letra)
    print(f'{palavra} tem as vogais: {(", ".join(map(str, letraVogais)))}')