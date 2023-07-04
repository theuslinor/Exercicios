preco = float(input('Qual é o preço do seu produto? R$ '))
desconto = (5 / preco) * 100
print('O valor que você irá pagar já com o desconto de 5% é de R${:.2f}'.format(preco - desconto))