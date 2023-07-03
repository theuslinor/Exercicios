def notas(*n, sit=False):
    """
    Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita varias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    escola = {}
    escola['Total'] = len(n)
    escola['Maior'] = max(n)
    escola['Menor'] = min(n)
    escola['Média'] = sum(n) / len(n)
    print(f'A maior nota foi {escola["Maior"]}.\n'
          f'A menor nota foi {escola["Menor"]}.\n'
          f'Foram um total de {escola["Total"]} notas.\n'
          f'A média da turma foi {escola["Média"]:.2f}.\n')
    if sit:
        if escola["Média"] > 5:
            situacao = '\033[32mAprovado\033[m'
        else:
            situacao = '\033[31mReprovado\033[m'
        print(f'Situação {situacao}.')


notas(5.5, 2.5, 2, 5.5, sit=True)