import requests

headers = {'Authorization': 'Token 311f9879396505826b7aedb6c5d691963815b1f4'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.get(url=url_base_cursos, headers=headers)

print(resultado.json())

# Testando se o endpoint está correto
assert resultado.status_code == 200

# Testando a quantidade de registros
assert resultado.json()['count'] == 2

# Testando se o título do primeiro curso está correto
assert resultado.json()['results'][0]['titulo'] == 'Criação de APIs REST com Django REST Framework'

