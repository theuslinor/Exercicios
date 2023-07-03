preco = float(input('Digite o preço do imovel: R$ '))
salario = float(input('Digite o seu salario: R$ '))
parcela = int(input('Digite em quantos anos você pretende pagar: '))
salario30 = salario * 30 / 100
preco_mensal = preco / (parcela * 12)
if preco_mensal >= salario30:
    print('Baseado em 30% do seu salario (R${}) seu empréstimo foi NEGADO! o valor da parcela seria R${:.2f}. '.format(salario30, preco_mensal))
else:
    print('Baseado em 30% do seu salario (R${:.2f}) seu emprestimo foi APROVADO! você pagará R${:.2f} de parcela.'.format(salario30 ,preco_mensal))