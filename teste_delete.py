import requests

headers = {'Authorization': 'Token 311f9879396505826b7aedb6c5d691963815b1f4'}
url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'


resultado = requests.delete(url=f'{url_base_cursos}4/', headers=headers)

# Testando o código HTTP
assert resultado.status_code == 204

# print(resultado.text)

# Testando se o tamanho do conteúdo retorno é 0
assert len(resultado.text) == 0

