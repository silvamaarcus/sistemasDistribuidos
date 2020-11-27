import requests

url = 'https://viacep.com.br/ws/MG/Belo Horizonte/Rua dos Aimores'

formato = '/json/'

r = requests.get(url + formato)

if (r.status_code == 200):
    print()
    print('JSON : ', r.json())
    print()
else:
    print('Nao houve sucesso na requisicao.')
