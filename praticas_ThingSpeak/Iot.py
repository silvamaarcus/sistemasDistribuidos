# Importando bibliotecas;
import requests
import time
import random

# Especificando minha URL de registro (Link gerado pelo ThingSpeak) dentro de uma variável;
url = 'https://api.thingspeak.com/update?api_key=ZJ2AF98Z7EZAOFC6&'

# Especificando a tabela de registro da TEMPERATURA dentro de uma variável;
tabela_temp = 'field1='
# Especificando a tabela de registro da UMIDADE dentro de uma variável;
tabela_umi = 'field2='

# Criação de variável vazia para gerar números aleatórios;
numAleatorio = ''

# Criando um laço de repetição para 15 valores;
for registro in range(15):
    numAleatorio = random.randrange(20,40)
    r = requests.get(url + tabela_temp + str(numAleatorio))
    if r.status_code == 200:
        print(f"{registro + 1}º Temperatura {numAleatorio}º")
        time.sleep(3)

for registro in range(15):
    numAleatorio = random.randrange(20,40)
    r = requests.get(url + tabela_umi + str(numAleatorio))
    if r.status_code == 200:
        print(f"{registro + 1}º Umidade {numAleatorio}º")
        time.sleep(3)
