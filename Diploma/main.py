import requests
import time
import json
import codecs

api_ver = '5.8'
token = '7b23e40ad10e08d3b7a8ec0956f2c57910c455e886b480b7d9fb59859870658c4a0b8fdc4dd494db19099'
user_id = '5030613'


def find_friends(user_id):
    params = {
        'v': api_ver,
        'user_id': user_id
    }
    response = requests.get('https://api.vk.com/method/friends.get', params).json()
    friends_ids = response['response']['items']
    return friends_ids


def find_user_groups(user_id):
    try:
        params = {
            'access_token': token,
            'v': api_ver,
            'user_id': user_id,
            'count' : '1000'
        }
        response = requests.get('https://api.vk.com/method/groups.get', params).json()
        user_groups = response['response']['items']
        print('*')
        time.sleep(0.34)
    except:
        print('Не удается получить информацию о группах пользователя id{0}'.format(user_id))
        user_groups = []
        return user_groups
    return user_groups


def find_friends_groups(friends_ids):
    all_friends_groups = []
    for friend in friends_ids:
        all_friends_groups += find_user_groups(friend)
    return all_friends_groups


def find_group_by_id(group_id):
    group_info = {}
    params = {
        'v': api_ver,
        'group_id': group_id,
        'fields': 'members_count'
    }
    group_data = (requests.get('https://api.vk.com/method/groups.getById', params).json())['response'][0]
    group_info['name'] = group_data['name']
    group_info['gid'] = group_id
    group_info['members_count'] = group_data['members_count']
    return group_info


friends_ids = find_friends(user_id)
# print('FRIENDS IDS: ', len(friends_ids), '\n', friends_ids, '\n')
user_groups = find_user_groups(user_id)
# print('USER GROUPS: ', len(user_groups), '\n', user_groups, '\n')
all_friends_groups = find_friends_groups(friends_ids)
# print('ALL FRIENDS GROUPS: ', len(all_friends_groups), '\n', all_friends_groups, '\n')
user_only_groups = set(user_groups).difference(set(all_friends_groups))
# print('USER ONLY GROUPS: ', len(user_only_groups), '\n', user_only_groups, '\n')
group_info_for_json = []
for group in user_only_groups:
    info = find_group_by_id(group)
    group_info_for_json.append(info)
with codecs.open('groups.json', 'w', encoding='utf-8') as f:
    json.dump(group_info_for_json, f, ensure_ascii=False)