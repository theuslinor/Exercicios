lista, listaCorreta = [], []
with open('usuarios.txt', 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()
    for i in range(0, len(linhas), 2):
        idade = linhas[i+1].strip()
        lista.append(int(idade))
print(sum(lista) / len(lista))