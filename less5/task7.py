import os
import json

data_base = [{}, {}, {}]

file = open('task7.txt', 'r', encoding='UTF-8')
content = file.readlines()
file.close()
count_firm = 0
sum_profit = 0
for i in content:
    count_firm += 1
    tps = i.split()
    tpp = int(tps[2])
    tpz = int(tps[3])
    profit = tpp - tpz
    if tpp > tpz:
        data_base[0][tps[0]] = profit
        sum_profit += profit
    else:
        data_base[2][tps[0]] = abs(profit)
average_profit = sum_profit / count_firm
data_base[1]['average_profit'] = average_profit
file.close()

new_file = open('jsontask7.txt', 'w', encoding='UTF-8')

new_content = json.dumps(data_base)
new_file.write(new_content)
new_file.close()
