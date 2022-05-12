# Arquivo para teste da API HelloWorld

import requests

BASE = 'http://127.0.0.1:5000/'

# main.py
# resposta = requests.get(BASE + "helloworld/")

# perfil.py

# Consulta simples
# resposta = requests.get(BASE + "Wesley/")

# Escrita e consulta
#requests.post(BASE + "Joao/18/")
#resposta = requests.get(BASE + "Joao/")

print(resposta.json())