import requests

r = requests.get('http://www.google.com/search', params={'q': 'america mineiro'})

if (r.status_code == 200):
    print()
    print('Retorno : ', r.text)
    print()

    # Abrindo arquivo que será armazenada a página web (HTML);
    arq = open('d:\\UNA\\sistemas\\praticas_htttp_get\\d_google.html', 'w')

    # Escrevendo página HTML;
    arq.write(r.text)

    # Fechando página HTML;
    arq.close()


else:
    print('Nao houve sucesso na requisicao.')
