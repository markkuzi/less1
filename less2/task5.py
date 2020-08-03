rating = [7, 5, 3, 3, 2]
rating_len = len(rating) - 1

while True:
    point = input('Введите колличество набранных вами баллов: ')
    if point.isdigit():
        point = int(point)
        break
    else:
        print('Некорректный ввод')
for i in range(rating_len, -1, -1):
    if point <= rating[i]:
        rating.insert(i + 1 , point)
        break
    if i == 0:
        rating.insert(i, point)
print(rating)
