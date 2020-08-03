number = input('Введите целое число: ')
if number.isdigit():
    once = int(number)
    double = int(number * 2)
    triple = int(number * 3)
    solution = once + double + triple
    print(f'{once} + {double} + {triple} = {solution}')
else:
    print('Некорректный ввод!')