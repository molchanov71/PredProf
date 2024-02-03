import csv

# Получение данных из файла space.txt в список data:
with open('space.txt', mode='r', encoding='utf8') as in_file:
    reader = csv.DictReader(in_file, delimiter='*')
    data = list(reader)
# data_new - список с полученными данными
data_new = []
for row in data:
    '''
    Описание переменных:
    ship_name, planet, coord_place, direction - соответственно название корабля, его родная планета, координаты последнего места связи, координаты вектора направления
    def_ind - индекс дефиса в названии корабля
    code - код, текстовая часть в названии корабля
    code_center_rev - строка, содержащая в себе 2 символа из центра кода в обратном порядке
    password - полученный пароль
    '''
    ship_name, planet, coord_place, direction = row.values()
    def_ind = ship_name.index('-')
    code = ship_name[:def_ind]
    code_center_rev = code[2:0:-1]
    password = f'{planet[-3:]}{code_center_rev}{planet[2::-1]}'
    # Добавление параметра password:
    row['password'] = password

    # Добавление полученного словаря в новый список
    data_new.append(row)

# Вывод полученных данных в новый файл space_uniq_password.csv
with open('space_uniq_password.csv', mode='w', encoding='utf8') as out_file:
    writer = csv.DictWriter(out_file, delimiter='*', fieldnames=data_new[0].keys())
    writer.writeheader()
    writer.writerows(data_new)
