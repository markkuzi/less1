def fact(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
        yield result


my_list = [i for i in fact(10)]
print(my_list)
