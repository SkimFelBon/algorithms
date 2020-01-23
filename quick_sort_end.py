"""quick sort"""

def quick_sort(unsorted_list, begin=None, end=None):
    """quick_sort
    starting from the end
    best case:
    O(n*log(n))
    Omega(log(n))
    worst case:
    O(n^2)
    Omega(n)
    """
    if begin is None:
        begin = 0
    if end is None:
        end = len(unsorted_list) - 1

    def partition(array, begin, end):
        # x is sorted item
        x = array[end]
        i = begin - 1
        for j in range(begin, end):
            if array[j] <= x:
                i += 1
                # exchange array[i] with array[j]
                array[j], array[i] = array[i], array[j]
        # exchange Array[i+1] with Array[end]
        array[end], array[i+1] = array[i+1], array[end]
        return i+1
    
    if begin >= end:
        return
    pivote = partition(unsorted_list, begin, end)
    # quick sort on left half
    quick_sort(unsorted_list, begin, pivote-1)
    # quick sort on right half
    quick_sort(unsorted_list, pivote+1, end)


def main():
    sample_list = [9, 81, 0, 0, 5, 7, 27, 12, 46]
    print(f"before: {sample_list}")
    quick_sort(sample_list)
    print(f"after: {sample_list}")

if __name__ == '__main__':
    main()

