from functools import reduce

my_list = [i for i in range(100, 107) if i % 2 == 0]
mult_all = reduce(lambda x, y: x * y, my_list)

print(mult_all)
