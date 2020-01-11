"""Bubble Sort"""

def bubble_sort_while(list_to_sort):
    """
    Bubble Sort
    Sorts list and returns new list
    """
    i = 0
    j = 0
    while True:
        try:
            j += 1
            i = 0
            exist = list_to_sort[j]
            while True:
                try:
                    first = list_to_sort[i]
                    second = list_to_sort[i+1]
                    if first > second:
                        list_to_sort[i+1] = first
                        list_to_sort[i] = second
                    i += 1
                except IndexError:
                    # EOF
                    break
        except IndexError:
            break


def bubble_sort_for(list_to_sort):
    """Bubble sort using for loop"""
    for _i in range(len(list_to_sort)):
        for _j in range(len(list_to_sort)):
            try:
                if list_to_sort[_j] > list_to_sort[_j+1]:
                    bigger = list_to_sort[_j]
                    list_to_sort[_j] = list_to_sort[_j+1]
                    list_to_sort[_j+1] = bigger
            except IndexError:
                # eof
                break

def bubble_sort_recur(list_to_sort, length):
    """Recursive bubble sort"""
    def sort(list_to_sort, length, i=None, j=None):
        if i is None:
            i = 0
        if j is None:
            j = 0
        if i+1 == length:
            if j == length:
                return list_to_sort
            return sort(list_to_sort, length, 0, j+1)
        if list_to_sort[i] > list_to_sort[i+1]:
            bigger = list_to_sort[i]
            list_to_sort[i] = list_to_sort[i+1]
            list_to_sort[i+1] = bigger
        return sort(list_to_sort, length, i+1, j)

    return sort(list_to_sort, length)



def main():
    """Bubble Sort
    big O or time complexity is n*square
    Bubble sort is considered the simplest sorting algorithm.
    It goes through an entire array and compares each neighboring number.
    It then swaps the numbers and keeps doing this until the list is in ascending order.
    """
    sample_list = [9, 81, 0, 0, 5, 7, 27, 12, 46]
    # bubble_sort_while(sample_list)
    # bubble_sort_for(sample_list)
    print(bubble_sort_recur(sample_list, len(sample_list)))
    print(sample_list)

if __name__ == '__main__':
    main()
