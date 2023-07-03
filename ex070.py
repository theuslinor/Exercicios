print('+' + '-'*18 + '+')
print('|' + ' '*18 + '|')
print('|' + ' '*2 + 'Casas Falidas' + ' '*3 + '|')
print('|' + ' '*18 + '|')
print('+' + '-'*18 + '+')
soma = preco = mais = 0
prod_barato = ''
preco_barato =  float('inf')
while True:
    preco+=preco
    prod = str(input('Nome do Produto: '))
    preco = float((input('Preço: R$ ')))
    if preco < preco_barato:
        prod_barato = prod
        preco_barato = preco
    if preco > 1000:
        mais+=1
    soma += preco
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).upper()[0]
        if continuar != 'N' and continuar != 'S':
            continuar = str(input('Quer continuar? [S/N] ')).upper()[0]
        else: 
            break
    if continuar == 'N':
        break
print(f'O total das compras deu R${soma}.')
print(f'Tem {mais} produtos acima de R$1000.')
print(f'O produto mais barato foi {prod_barato} que custa R${preco_barato}.')