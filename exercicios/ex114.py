import urllib.request

url = 'https://www.google.com'

try:
    response = urllib.request.urlopen(url)
    print(f'é possivel entrar no {url}')
except:
    print('Não é possível se conectar ao site')
