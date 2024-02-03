from exc1 import data_new


def create_hash(row):
    ''' Описание функции create_hash.

    Описание аргументов:
    row - данные корабля

    Описание переменных:
    ship_name - название корабля
    planet - название родной планеты корабля
    _hash - полученный хэш
    '''
    ship_name = row['ShipName']
    planet = row['planet']
    _hash = f'{ship_name}:{planet}'
    return _hash


# hash_data - хэш-таблица, полученная из исходной таблицы data_new
hash_data = list(map(create_hash, data_new))

# Вывод хэшей 10 первых кораблей
print(*hash_data[10:], sep='\n')
