from exc1 import data_new
# data_new - исправленные данные
ship_name = input()
# ship_name - название корабля, вводимое пользователем
while ship_name != 'stop':
    '''
    Описание переменных:
    flag - переменная типа bool, которая показывает, был ли найден в данных корабль с названием, введённым пользователем
    ship - данные найденного корабля (если он был найден)
    planet - название родной планеты найденного корабля
    direction - координаты вектора направления найденного корабля
    '''
    flag = False
    ship = {}
    for row in data_new:
        if row['ShipName'] == ship_name:
            ship = row
            flag = True
            break
    if not flag:
        print('error.. er.. ror..')
        ship_name = input()
        continue
    planet = ship['planet']
    direction = ship['direction']
    print(f'Корабль {ship_name} был отправлен с планеты {planet} и его направление движения было: {direction}')
    ship_name = input()
