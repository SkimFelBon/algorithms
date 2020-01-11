"""insertion sort"""


def insertion_sort(array):
    """simple insertion sort"""
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

def recur_insertion_sort(array):
    """Recursive insertion sort"""


some_list = [1, 6, 2, 1, 8, 6, 7, 8, 5]

insertion_sort(some_list)
print(some_list)
