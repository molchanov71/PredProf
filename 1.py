import csv

with open('space.txt', mode='r', encoding='utf8') as in_file:
    reader = csv.DictReader(in_file, delimiter='*')
    data = list(reader)
# data_new - исправленные данные из файла space.txt
data_new = []

for row in data:
    '''
    Описание переменных:
    ship_name - Название корабля, значение ShipName в каждой строке
    n_ind - индекс цифры n, первой цифры в номере корабля, в строке ship_name
    m_ind - индекс цифры m, второй цифры в номере корабля, в строке ship_name
    n - числовое значение первой цифры в номере корабля
    m - числовое значение второй цифры в номере корабля
    t - длина названия родной планеты корабля (row["planet"])
    x_d, y_d - числовые значения координат вектора направления корабля
    x_new, y_new - исправленные координаты последнего места связи
    row_new - исправленные данные корабля, собранные в словарь
    '''
    ship_name = row['ShipName']
    n_ind = ship_name.index('-') + 1
    n = int(ship_name[n_ind])
    m = int(ship_name[n_ind + 1])
    t = len(row['planet'])
    x_d, y_d = tuple(map(int, row['direction'].split()))
    x_new = 0
    y_new = 0
    if n > 5:
        x_new = n + x_d
    elif n <= 5:
        x_new = -(n + x_d) * 4 + t
    if m > 3:
        y_new = m + t + y_d
    elif m <= 3:
        y_new = -(n + y_d) * m
    row_new = {'ShipName': ship_name, 'planet': row['planet'], 'coord_place': f'{x_new} {y_new}',
               'direction': row['direction']}
    data_new.append(row_new)
# to_write - данные, которые нужно вывести в файл space_new.txt
to_write = []
for row in data_new:
    '''
    Описание переменных: 
    last_ind - индекс последней буквы в коде корабля
    '''
    last_ind = row['ShipName'].index('-') - 1
    if row['ShipName'][last_ind] == 'V':
        to_write.append(f'{row["ShipName"]} - ({", ".join(row["coord_place"].split())})\n')
# Вывод данных в файл space_new.txt
with open('space_new.txt', mode='w', encoding='utf8') as out_file:
    out_file.writelines(to_write)
