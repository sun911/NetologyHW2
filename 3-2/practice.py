# Необходимо расширить функцию переводчика так, чтобы она принимала следующие параметры:
#
# путь к файлу с текстом;
# путь к файлу с результатом;
# язык с которого перевести;
# язык на который перевести (по-умолчанию русский).
# У вас есть 3 файла (DE.txt, ES.txt, FR.txt) с новостями на 3 языках: французском, испанском, немецком.
# Функция должна взять каждый файл с текстом, перевести его на русский и сохранить результат в новом файле.
#
# Для переводов можно пользоваться API Yandex.Переводчик.

import requests


def translate_it(source_path, result_path, source_lang, result_lang='ru'):
    """
    YANDEX translation plugin

    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/

    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param text: <str> text for translation.
    :return: <str> translated text.
    """
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'

    with open(source_path, 'rb') as f:
        text = f.read()

    trans_direction = (source_lang + '-' + result_lang)

    params = {
        'key': key,
        'lang': trans_direction,
        'text': text,
    }

    response = requests.get(url, params=params).json()

    with open(result_path, 'w') as f:
        f.write(' '.join(response.get('text', [])))

    return ' '.join(response.get('text', []))


a = translate_it('DE.txt', 'de-1.txt', 'de')
print(a)
b = translate_it('ES.txt', 'es-1.txt', 'es')
print(b)
c = translate_it('FR.txt', 'fr-1.txt', 'fr')
print(c)