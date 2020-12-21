import requests
import json


def lista_filmes(titulo):
    lista = []
    for i in range(1, 101):
        try:
            url = 'http://www.omdbapi.com/?i=tt3896198&apikey=dd&s=' + titulo + '&type=movie&page=' + str(i)  #Criar chave da API para testar o código
            req = requests.get(url)
            resposta = json.loads(req.text)
            if resposta['Response'] == 'True':
                for filme in resposta['Search']:
                    tit = filme['Title']
                    ano = filme['Year']
                    string = tit + ' (' + ano + ') '
                    lista.append(string)
            else:
                break
        except Exception as err:
            print('Conexão falhou! Erro encontrado: ', err)
    return lista