# quickSort.py
# quick sort starting from beggining
def partition(array, begin, end):
    pivot_idx = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot_idx += 1
            array[i], array[pivot_idx] = array[pivot_idx], array[i]
            print(array[i], array[pivot_idx])
    array[pivot_idx], array[begin] = array[begin], array[pivot_idx]
    return pivot_idx

def quick_sort_recursion(array, begin, end):
    if begin >= end:
        return None
    pivot_idx = partition(array, begin, end)
    quick_sort_recursion(array, begin, pivot_idx-1)
    quick_sort_recursion(array, pivot_idx+1, end)

def quick_sort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    return quick_sort_recursion(array, begin, end)

myList = [6, 5, 3, 1, 8, 7, 2, 4]
print(myList)
quick_sort(myList)
print(myList)
"""
begin = 0
end = 7
pivot_idx = 0,1,2
range(1, 7)
i = 1,2
array[2], array[2] = array[2], array[2]

"""
