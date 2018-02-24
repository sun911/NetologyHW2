# Взять из github-репозитория все файлы с новостями в формате txt:
# newsfr.txt, newsit.txt, newsafr.txt, newscy.txt. Для этого нужно склонировать репозиторий, или скачать его архивом.
#
# Для определения кодировки использовать модуль chardet
#
# Написать программу, которая будет выводить топ 10 самых часто встречающихся в новостях слов длиннее 6 символов для каждого файла.
#
# Не забываем про декомпозицию и организацию кода в функции. В решении домашнего задания вам могут помочь: split(), sort() или sorted().


def search_top_words(filename):
    import chardet

    with open(filename, 'rb') as f:
        news = f.read()
        result = chardet.detect(news)

    with open(filename, encoding=result['encoding']) as f:
        news_text = f.read().replace('\n', '').lower().split(' ')

    long_words = []
    for word in news_text:
        if len(word) > 6:
            long_words.append(word)
    repeat_words = {}
    for word in long_words:
        repeat_words[word] = long_words.count(word)
    top_words = []
    for key in sorted(repeat_words, key=repeat_words.get, reverse=True):
        top_words.append(key)
    print('\n10 наиболее часто встречающихся слов:')
    for i in range(10):
        print(top_words[i])


file_name = input('\nВведите имя файла: ')
search_top_words(file_name)
