def fatorial(a=0, b=False):

    """
    Calcula o fatorial de um número e imprime a operação completa do cálculo,
    se desejado.

    Args:
        a (int): o número que será usado para calcular o fatorial
        b (bool): um valor booleano que indica se a função deve imprimir ou não
            a operação completa do cálculo do fatorial

    Returns:
        int or str: se o parâmetro "b" for False, retorna o resultado do cálculo
            do fatorial como um número inteiro. Se "b" for True, retorna uma string
            contendo a operação completa do cálculo e o resultado.
    """

    numb = []
    for i in range(a, 0, -1):
        numb.append(i)
    soma = 1
    if b:
        for num in numb:
            if soma == 1:
                print(num, end='')
            else:
                print(f' x {num}', end='')
            soma *= num
        return f' = {soma}'
    else:
        for num in numb:
            soma *= num
        return soma


print(fatorial(int(input('Digite o numero fatorial: ')), bool(input())))