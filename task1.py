first_var = 123
second_var = 'Hello'
third_var = 3.22
print(first_var, second_var, third_var)
fourth_var = input('Введите строку: ')
fifth_var = input('Введите целое число: ')
if fifth_var.isdigit():
    fifth_var = int(fifth_var)
    print(f'Ваша строка: {fourth_var}, ваше число: {fifth_var}')
else:
    print(f'Ваша строка: {fourth_var}, ваше число не является числом')

