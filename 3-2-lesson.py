import requests

# var = 'http://httpbin.org/user-agent'
#
# print(
#     requests.get(var).text
# )

# var = 'http://httpbin.org/user-agent'
#
# print(
#     requests.request('get', var).text
# )


# url = 'https://translate.yandex.net/api/v1/tr.json/translate?'
#
#
# def translate_en_ru(text):
#     response = requests.post(
#         url,
#         params=dict(
#             id='5b31d42d.5aae35f5.12c2b673-3-0',
#             srv='tr-text',
#             lang='en-ru',
#             reason='paste'
#         ),
#         data=dict(
#             text=text
#         )
#     )
#
#     return ''.join(response.json()['text'])
#
# print(translate_en_ru('Hello world'))

response = requests.get('http://httpbin.org/image/png')
with open('img.png', 'wb') as file:
    file.write(response.content)
