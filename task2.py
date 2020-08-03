time_s = input('Введите время в секундах: ')
if time_s.isdigit():
    time_s = int(time_s)
    hour = time_s // 1600
    minute = time_s // 60 % 60
    second = time_s % 60
    print(hour, minute, second, sep=':')
else:
    print('Некорректный ввод')
