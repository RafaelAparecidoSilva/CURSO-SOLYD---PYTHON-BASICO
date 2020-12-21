import requests
import json

def requisicao (titulo):
    """Utiliza API da OMDb para requisitar informações sobre qualquer filme solicitado"""
    try:
        req = requests.get('http://www.omdbapi.com/?i=tt3896198&apikey=dd&t=' + titulo + '&type=movie')  #Criar chave da API para testar o código
        dicionario = json.loads(req.text)
        return dicionario
    except Exception as err:
        print(f'O seguinte erro de conexão foi encontrado: {err}')
        return None