def quick_sort(integers):
    if not integers:
        return []
    sorted_list = []
    pivot_value = integers[0]

    less_than_list = []
    equal_to_list = []
    greater_than_list = []

    for integer in integers:
        if integer < pivot_value:
            less_than_list.append(integer)
        elif integer == pivot_value:
            equal_to_list.append(integer)
        elif integer > pivot_value:
            greater_than_list.append(integer)
    
    return quick_sort(less_than_list) + equal_to_list + quick_sort(greater_than_list)
