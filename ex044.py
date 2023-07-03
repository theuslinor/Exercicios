preco = float(input('Valor das compras: ')).__abs__()
if preco <= 40:
    escolha = int(input('Só parcelamos a partir de R$40, abaixo disso passamos somente a vísta no cartão. Gostaria passar a vísta no cartão? '
                        '\n\033[33mFORMAS DE PAGAMENTO: '
                        '\n[ 1 ] à vista no dinheiro/cheque'
                        '\n[ 2 ] à vista cartão'
                        '\nQual opção? '))
    if escolha == 1:
        valor_total = preco - (10 * preco) / 100
        print('Pagando à vista no dinheiro/cheque o valor total fica \033[32mR${:.2f}\033[m com desconto de \033[32m10%\033[m.'.format(valor_total))
    elif escolha == 2:
        valor_total = preco - (5 * preco) / 100
        print('Pagando à vista no cartão o valor total fica \033[32mR${:.2f}\033[m com desconto de \033[36m5%\033[m.'.format(valor_total))
else:
    escolha = int(input('\033[33mFORMAS DE PAGAMENTO '
                        '\n[ 1 ] à vista no dinheiro/cheque'
                        '\n[ 2 ] à vista cartão'
                        '\n[ 3 ] 2x no cartão'
                        '\n[ 4 ] 3x ou mais no cartão'
                        '\nQual opção? \033[m'))
    if escolha == 1:
        valor_total = preco - (10 * preco) / 100
        print('Pagando à vista no dinheiro/cheque o valor total fica \033[32mR${:.2f}\033[m com desconto de \033[32m10%\033[m.'.format(valor_total))
    elif escolha == 2:
        valor_total = preco - (5 * preco) / 100
        print('Pagando à vista no cartão o valor total fica \033[32mR${:.2f}\033[m com desconto de \033[36m5%\033[m.'.format(valor_total))
    elif escolha == 3:
        valor_parc = preco / 2
        print('Pagando parcelado em 2x o valor parcelado fica duas parcelas de \033[32mR${:.2f}\033[m e valor total fica \033[32mR${:.2f}\033[m.'.format(valor_parc, preco))
    if escolha == 4:
        parc = int(input('\033[33mNúmero de parcelas max 12x: \033[m'))
        if parc > 12:
            print('\033[31mDigite uma parcela válida\033[m')
        elif parc == 2:
            valor_parc = preco / 2
            print('Pagando parcelado em 2x o valor parcelado fica duas parcelas de \033[32mR${:.2f}\033[m e valor total fica \033[32mR${:.2f}\033[m.'.format(valor_parc, preco))
        elif parc == 1:
            valor_total = preco - (5 * preco) / 100
            print('Pagando à vista no cartão o valor total fica \033[32mR${:.2f}\033[m com desconto de \033[36m5%\033[m.'.format(valor_total))
        else:
            preco = (preco + (20 * preco) / 100)
            valor_parc = preco / parc
            print('Ficará \033[36m{}\033[m parcelas de \033[32mR${:.2f}\033[m, com valor total de \033[32mR${:.2f}\033[m com acrescimento de \033[36m20%\033[m.'.format(parc, valor_parc, preco))
    else:
        print('\033[31mDigite um número válido\033[m')