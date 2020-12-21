from PROJETO_INFO_FILMES.Functions import Detalhes as det, Requisicao as req


sair = False
while not sair:
    op = input('Escreva o nome de um filme ou SAIR para fechar: ')

    if op == 'SAIR':
        sair = True
        print('Saindo...')
    else:
        filme = req.requisicao(op)
        if filme['Response'] == 'False':
            print('Filme não encontrado.')
        else:
            det.printar_detalhes(filme)
