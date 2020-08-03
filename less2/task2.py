test_list = []
tpn = 0
while True:
    tpn = input('Введите любое значение, которое будет добавлено в список, надоело добавлять? введите "хватит"\n')
    if tpn == 'хватит':
        break
    test_list.append(tpn)
test_list_len = len(test_list)
print(test_list)
for i in range(test_list_len):
    if i % 2 != 0:
        test_list[i], test_list[i-1] = test_list[i-1], test_list[i]
print(test_list)
