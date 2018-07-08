from math import sqrt


def get_data(file_name):
    f = open(file_name)
    lines = f.readlines()
    f.close()
    return lines


def data2int(data):
    int_data = [int(i) for i in data]
    return int_data


def sort_data(int_data):
    list.sort(int_data)
    return int_data


def min_sorted_list(int_data):
    return int_data[0]


def max_sorted_list(int_data):
    return int_data[-1]


def standard_dev(int_data):
    length = len(int_data)
    average = sum(int_data) / length
    std_dev = [(i - average)**2 for i in int_data]
    average_sd = sum(std_dev) / length
    return sqrt(average_sd)


data = get_data("data")
int_data = data2int(data)
sorted_int_data = sort_data(int_data)
min_value = min_sorted_list(int_data)
max_value = max_sorted_list(int_data)
std_dev_value = standard_dev(int_data)


print(min_value)
print(max_value)
print(std_dev_value)
