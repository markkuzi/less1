products = []
while True:
    tpn = (len(products) + 1, {})
    name = input('Введите название продукта: ')
    tpn[1].get('название')
    tpn[1]['название'] = name
    while True:
        price = input('Введите цену продукта: ')
        if price.isdigit():
            break
        print('Введите цену целым числом!')
    tpn[1].get('цена')
    tpn[1]['цена'] = price
    while True:
        number = input('Введите количество продукта: ')
        if number.isdigit():
            break
        print('Введите количество целым числом!')
    tpn[1].get('количество')
    tpn[1]['количество'] = number
    calc = input('Введите единицу исчисления продукта: ')
    tpn[1].get('ед')
    tpn[1]['ед'] = calc
    products.append(tpn)
    exit_add = input('Введите любое значение, что бы добавить еще товар. Введите 0, что бы выйти: ')
    if exit_add == '0':
        break
product_analysis = {}
for i in products[0][1]:
    product_analysis.get(i)
    product_analysis[i] = []
for i in range(0, len(products)):
    product_analysis['название'].append(products[i][1]['название'])
    product_analysis['цена'].append(products[i][1]['цена'])
    product_analysis['количество'].append(products[i][1]['количество'])
    product_analysis['ед'].append(products[i][1]['ед'])
print(product_analysis)
