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

def recur_while_insertion_sort(array):
    """Recursive insertion sort"""
    def iterate(array, length, acc=None):
        if acc is None:
            acc = 0
        # basecase
        if acc == length:
            return
        # do stuff here
        key = array[acc]
        j = acc - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
        
        return iterate(array, length, acc+1)
    iterate(array, len(array))

def recur_insertion_sort(array):
    """trully recursive insertion sort"""
    def while_loop(array, j, key):
        """recursive while loop """
        if j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
            j, key = while_loop(array, j, key)
        return j, key

    def iterate(array, length, acc=None):
        if acc is None:
            acc = 0
        # basecase
        if acc == length:
            return
        # do stuff here
        key = array[acc]
        j = acc - 1
        # recur here
        j, key = while_loop(array, j, key)
        array[j + 1] = key
        return iterate(array, length, acc+1)

    iterate(array, len(array))

    


some_list = [1, 6, 2, 1, 8, 6, 7, 8, 5]

recur_insertion_sort(some_list)
print(some_list)

