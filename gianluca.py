def sort_data():
    f = open("data")
    lines = f.readlines()
    f.close()
    int_data = [int(i) for i in lines]
    list.sort(int_data)
    return int_data


def min():
    f = open("data")
    lines = f.readlines()
    f.close()
    int_data = [int(i) for i in lines]
    list.sort(int_data)
    return int_data[0]


def max():
    f = open("data")
    lines = f.readlines()
    f.close()
    int_data = [int(i) for i in lines]
    list.sort(int_data)
    return int_data[-1]


def standard_dev():
    f = open("data")
    lines = f.readlines()
    f.close()
    int_data = [int(i) for i in lines]
    list.sort(int_data)
    length = len(int_data)
    average = sum(int_data) / length
    from math import sqrt
    std_dev = [(i - average)**2 for i in int_data]
    average_sd = sum(std_dev) / length
    return sqrt(average_sd)


print(min())
print(max())
print(standard_dev())
