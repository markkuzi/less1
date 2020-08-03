invest = 20
profit = 0
count = 1
for i in range(1, 31):
    year = invest * 12
    profit = (profit + year) * 1.1
    print(count, invest, year, profit)
    count+=1
    invest += 20
profit = (profit * 0.1) / 12
print(profit)
