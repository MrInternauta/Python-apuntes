countries = {
    'mexico': 122,
    'colombia': 49,
    'argentina': 43,
    'chile': 18,
    'peru': 31

}

while True:
    country = str(raw_input('Ingresa un nombre de pais: ')).lower()
    try:
        print('La poblacion de {} es {} millones'.format(country, countries[country]))
    except KeyError:
        print('Error: no esta ese dato')
