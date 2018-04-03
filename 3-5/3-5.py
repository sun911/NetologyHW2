import osa


def currency_convert(source_path):
    client = osa.Client('http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL')
    sum = 0
    with open(source_path, 'r') as f:
        for line in f.readlines():
            text = line.replace('\n', '').split(' ')
            sum += client.service.ConvertToNum('', text[2], 'rub', text[1], 'false')
    return round(sum)


a = currency_convert('currencies.txt')
print('Затраты на путешествие:', a, 'рублей.')
