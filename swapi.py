import requests
from pathlib import Path


class APIRequester:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint=''):
        url = f'{self.base_url}{endpoint}'
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response
        except requests.RequestException:
            print('Возникла ошибка при выполнении запроса')
            return None


class SWRequester(APIRequester):
    def get_sw_categories(self):
        response = self.get('/')
        if response:
            return response.json().keys()
        return []

    def get_sw_info(self, sw_type):
        response = self.get(f'/{sw_type}/')
        if response:
            return response.text
        return ''


def save_sw_data():
    swr = SWRequester('https://swapi.dev/api')
    Path('data').mkdir(exist_ok=True)
    categories = swr.get_sw_categories()
    for category in categories:
        data = swr.get_sw_info(category)
        with open(f'data/{category}.txt', 'w', encoding='utf-8') as f:
            f.write(data)


if __name__ == '__main__':
    save_sw_data()
