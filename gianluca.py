from math import sqrt


def get_data_from_file(file_name):
    f = open(file_name)
    lines = f.readlines()
    f.close()
    return lines


def convert_dato_to_int(data):
    int_data = [int(i) for i in data]
    return int_data


def sort_data(int_data):
    list.sort(int_data)
    return int_data


def min_sorted_list(data):
    return data[0]


def max_sorted_list(data):
    return data[-1]


def standard_dev(data):
    length = len(data)
    average = sum(data) / length
    std_dev = [(i - average)**2 for i in data]
    average_sd = sum(std_dev) / length
    return sqrt(average_sd)


data = get_data_from_file("data")
int_data = convert_dato_to_int(data)
sorted_int_data = sort_data(int_data)
