# import requests
# import json
#
#
# def lista_filmes(titulo):
#     lista = []
#     for i in range(1, 101):
#         try:
#             url = 'http://www.omdbapi.com/?i=tt3896198&apikey=244851dd&s=' + titulo + '&type=movie&page=' + str(i)
#             req = requests.get(url)
#             resposta = json.loads(req.text)
#             if resposta['Response'] == 'True':
#                 for filme in resposta['Search']:
#                     tit = filme['Title']
#                     ano = filme['Year']
#                     string = tit + ' (' + ano + ') '
#                     lista.append(string)
#             else:
#                 break
#         except Exception as err:
#             print('Conexão falhou! Erro encontrado: ', err)
#     return lista

from PROJETO_LISTA_FILMES.Functions import Lista_Filmes as lf


while True:
    opcao = input('Pesquise por um filme ou digite SAIR: \n').strip().upper()
    if opcao == 'SAIR':
        print("\nSaindo do programa...\n")
        break
    elif opcao == '':
        print('Digite um nome válido')
        continue
    lista_de_filmes = lf.lista_filmes(opcao)
    print('FILMES ENCONTRADOS:', len(lista_de_filmes), '\n')
    for filme in lista_de_filmes:
        print(filme)
    print('\n')