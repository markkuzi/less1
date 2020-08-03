from sys import argv
from itertools import (count,
                       cycle)

# _, number = argv
number = 1
number = int(number)
for i in count(number):
    if i > number + 20:
        break
    print(i)

my_list = ['Hello', 'World']
tpi = 0
for i in cycle(my_list):
    if tpi > 5:
        break
    print(i)
    tpi += 1
