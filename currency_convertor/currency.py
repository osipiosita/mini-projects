import requests
API_KEY = 'fca_live_i9gpeioXQix6RlPirGfBLDMx4flKc60V46FJ5Yey'
URL = f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}'
CURRENCIES = ['USD', 'AUD', 'CNY', 'CAD', 'EUR']

def convert_currency(base):
    currencies = ','.join(CURRENCIES)
    url = f'{URL}&base_currency={base}&currencies={currencies}'

    try:
        response = requests.get(url)
        data = response.json()
        return data['data']
    
    except Exception as e:
        print('Inavalid currency!')
        return None
    
while True:
    base = input('Enter the base currency (q to quit): ').upper()
    if base == 'Q':
        print('Goodbye!')
        break

    data = convert_currency(base)

    if data == None:
        continue
    
    del data[base]
    for key, value in data.items():
        print(f'{key}:{value}')