import urequests as requests
import ujson as json


API_TARGET = 'https://dog.ceo'


if __name__ == '__main__':
    response = None
    parsed_json = None
    url = API_TARGET + '/api/breeds/image/random'

    try:
        print(f'[INFO] start GET request to {url}')
        response = requests.get(url)
    except Exception as err:
        print(f'[ERROR] Request failed: {err}')

    if response:
        print('[INFO] parse JSON response')
        try:
            parsed_json = json.loads(response.text)
        except ValueError as err:
            print(f'[ERROR] Response parsing failed: {err}')

    if parsed_json:
        print(parsed_json)
