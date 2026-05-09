def selection_sort(integers):
    if not integers:
        return integers
    for index in range(len(integers) - 1):
        min_index = index
        for j in range(index + 1, len(integers)):
            if integers[j] < integers[min_index]:
                min_index = j
        if min_index != index:
            integers[index], integers[min_index] = integers[min_index], integers[index]
    return integers
