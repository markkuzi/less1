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
    a = input('Введите расстояние, которое спортсмен пробежал сегодня: ')
    if is_digit(a):
        a = float(a)
        break
    else:
        print('Это долно быть число!')
while True:
    b = input('Введите расстояние, которое спортсмен должен пробегать за день: ')
    if is_digit(b):
        b = float(b)
        break
    else:
        print('Это долно быть число!')
day = 1
while a < b:
    a *= 1.1
    day += 1
print(f'на {day}-й день спортсмен достиг результата — не менее {b} км.')