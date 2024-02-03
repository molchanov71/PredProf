from exc1 import data_new


def get_ship_number(_row):
    ''' Описание функции get_ship_number.

    Описание аргументов:
    _row - входные данные каждого корабля

    Описание переменных:
    ship_name - название корабля
    first_ind - индекс первой цифры в названии корабля
    number - номер корабля
    '''
    ship_name = _row['ShipName']
    first_ind = ship_name.index('-') + 1
    number = int(ship_name[first_ind:])
    return number


# Сортировка данных "пузырьком"
for i in range(len(data_new) - 1):
    for j in range(i + 1, len(data_new)):
        if get_ship_number(data_new[i]) > get_ship_number(data_new[j]):
            data_new[i], data_new[j] = data_new[j], data_new[i]

# Вывод 10 первых кораблей в получившемся списке
print(*(row['ShipName'] for row in data_new[:10]), sep='\n')
