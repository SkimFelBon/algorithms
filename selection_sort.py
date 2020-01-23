"""Selection sort """

def selection_sort(unsorted_list):
    """O(n) = n^2
       Auxiliary Space: O(1)
       The good thing about selection sort is it never makes more
       than O(n) swaps and can be useful when memory write
       is a costly operation.
    """
    def find_smallest_value(array):
        small = array[0]
        for i in range(len(array)):
            if small > array[i]:
                small = array[i]
        array.remove(small)
        return small
    
    sorted_list = []
    for i in range(len(unsorted_list)):
        smallest = find_smallest_value(unsorted_list)
        sorted_list.append(smallest)
    return sorted_list

    

    
            
                



def main():
    """Selection sort"""
    sample_list = [9, 81, 0, 0, 5, 7, 27, 12, 46]
    print(f"before: {sample_list}")
    result = selection_sort(sample_list)
    print(f"after: {result}")


if __name__ == '__main__':
    main()
