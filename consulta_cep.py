import requests
import json
from flask import Flask

cep = str(input('digite seu cep: ')).strip()

if len(cep) == 9:
    cep = cep.replace('-', '')

r = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
r = r.json()

app = Flask(__name__)

@app.route('/')
def retorna_cep():
    return r


if __name__ == '__main__':
    app.run()