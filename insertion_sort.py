"""Insertion sort"""


def _insertion_sort(arr):
    """Insertion sort"""

    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def insertion_sort(array):
    """Insertion sort algorithm"""
    for i in range(1, len(array)):
        key = array[i]

        j = i-1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        # base case
        array[j + 1] = key





def main():
    """Insertion sort"""
    sample_list = [9, 81, 0, 0, 5, 7, 27, 12, 46]
    insertion_sort(sample_list)
    print(sample_list)
    return


if __name__ == '__main__':
    main()


# >>> mylist.insert(1,0)
# >>> mylist
# [0, 0]
# >>> mylist.insert(0,2)
# >>> mylist
# [2, 0, 0]
# >>> exit()
