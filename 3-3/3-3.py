from urllib.parse import urlencode

import requests

APP_ID = 6418916
AUTH_URL = 'https://oauth.vk.com/authorize'

auth_data = {
    'client_id': APP_ID,
    'display': 'mobile',
    'scope': 'friends,status',
    'response_type': 'token',
    'v': '5.73'
}

#print('?'.join((AUTH_URL, urlencode(auth_data))))

TOKEN = '87f9710e5ede2910a9b895a02c9ebff701837e413d5b0e29f4f52cd27a19d7a6643201303001bac4c7309'
target_uid = 213521488


def find_friends(target_uid):
    params = {
        'access_token': TOKEN,
        'v': '5.73',
        'target_uid': target_uid
    }

    response = requests.get('https://api.vk.com/method/friends.getMutual', params)

    for vk_id in response.json()['response']:
        print('User ID: ' + str(vk_id) + ', адрес ' + 'https://vk.com/id' + str(vk_id))


find_friends(target_uid)