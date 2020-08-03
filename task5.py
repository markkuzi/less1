def is_digit(string):
    if string.isdigit():
        return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False


while True:
    gain = input('Введите выручку фирмы: ')
    if is_digit(gain):
        gain = float(gain)
        break
    else:
        print('Это долно быть число!')

while True:
    cost = input('Введите издержки фирмы: ')
    if is_digit(cost):
        cost = float(cost)
        break
    else:
        print('Это долно быть число!')
profit = gain - cost
if gain > cost:
    print(f'Фирма работает в прибыль, прибыль = {profit}')
    rent = profit / gain
    print(f'Рентабельность выручки = {rent}')
    while True:
        personal = input('Введите количетсво сотрудников: ')
        if personal.isdigit():
            personal = int(personal)
            break
        else:
            print('Это долно быть число!')
    profit_for_person = profit / personal
    print(f'Прибыль фирмы на одного сотрудника = {profit_for_person}')
elif gain < cost:
    print(f'Фирма работает в убыток, убыток = {abs(profit)}')
else:
    print('Фирма вышла в 0')