number = input('Введите целое число: ')
if number.isdigit():
    number = int(number)
    biggest = 0
    while number != 0:
        if biggest < number % 10:
            biggest = number % 10
        number = number // 10
    print(f'Самая большая цифра в числе: {biggest}')
else:
    print('Некорректный ввод!')