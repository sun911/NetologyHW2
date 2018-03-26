import requests


class YaBase:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Authorization': 'OAuth {}'.format(self.token)
        }


class YaMetrikaUser(YaBase):

    def get_counters(self):
        headers = self.get_headers()
        response = requests.get('https://api-metrika.yandex.ru/management/v1/counters', headers=headers)
        return [c['id'] for c in response.json()['counters']]


class Counter(YaBase):

    def __init__(self, counter_id, token):
        self.counter_id = counter_id
        super().__init__(token)

    def get_visits(self):
        headers = self.get_headers()
        params = {
            'id': self.counter_id,
            'metrics': 'ym:s:visits,ym:s:pageviews,ym:s:users'
        }
        response = requests.get('https://api-metrika.yandex.ru/stat/v1/data', params, headers=headers)

        return response.json()['data'][0]['metrics']


first_user = YaMetrikaUser('AQAAAAAMRn--AATo1uyW7OP3NE2fks1W2mt5bpY')
counters = first_user.get_counters()
print(counters)
for counter_id in counters:
    counter = Counter(counter_id, first_user.token)
    visits = counter.get_visits()
    print('Количество визитов:', visits[0])
    print('Количество просмотров:', visits[1])
    print('Количество посетителей:', visits[2])
