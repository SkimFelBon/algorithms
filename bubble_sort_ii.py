def bubble_sort(array):
    for j in range(len(array)):
        for i in range(len(array)):
            try:
                if array[i] > array[i+1]:
                    bigger = array[i]
                    array[i] = array[i+1]
                    array[i+1] = bigger
            except IndexError:
                pass


some_list = [1,6,2,1,8,6,7,8,5]

bubble_sort(some_list)
print(some_list)
