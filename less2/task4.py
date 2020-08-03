words = input('Введите несколько слов через пробел:\n').split()
for i in words:
    if len(i) > 10:
        print(i[:10])
    else:
        print(i)
