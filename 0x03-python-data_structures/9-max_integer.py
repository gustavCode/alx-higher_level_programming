#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None

    max_num = min(my_list)
    for x in my_list:
        if x > max_num:
            max_num = x

    return max_num
