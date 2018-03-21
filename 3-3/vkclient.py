from urllib.parse import urlencode

import requests

APP_ID = 6417432
AUTH_URL = 'https://oauth.vk.com/authorize'

auth_data = {
    'client_id': APP_ID,
    'display': 'mobile',
    'scope': 'friends,status',
    'response_type': 'token',
    'v': '5.73'
}

print('?'.join((AUTH_URL, urlencode(auth_data))))

TOKEN = 'b228127f90da4d7332013b5ee945a619793aea15eb1041023370bed7028294e2c4f82eb7923faabfae596'

params = {
    'access_token': TOKEN,
    'v': '5.73'
}

response = requests.get('https://api.vk.com/method/status.get', params)

print(response.text)


# def find_friends(target_uid, TOKEN):
#     params = {
#         'access_token': TOKEN,
#         'v': '5.73',
#         'target_uid': target_uid
#     }
#
#     response = requests.get('https://api.vk.com/method/friends.getMutual', params)
#
#     for x, y in enumerate(response.json()['response'], 1):
#         pprint(f"{x}. id друга {y}. Ссылка на страницу друга: https://vk.com/id{y}")
#
# find_friends(target_uid, TOKEN)
