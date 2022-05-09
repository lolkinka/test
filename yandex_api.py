import requests

URL = 'https://cloud-api.yandex.net/v1/disk/resources'
TOKEN = 'AQAAAABb2UwpAADLW15vaP1hAkZvkLfvpFShH2E'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {TOKEN}'}

def create_folder(path):
    response = requests.put(f'{URL}?path={path}', headers=headers)
    if response.status_code == 201:
        return "Success"
    else:
        return 'Empty'
create_folder('hello world')