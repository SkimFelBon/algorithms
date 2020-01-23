"""one_more_merge_sort"""

def merge_sort(array):
    if len(array) <= 1:
        return array
    middle = len(array) // 2
    left_part = merge_sort(array[:middle])
    right_part = merge_sort(array[middle:])
    return list(sort(left_part, right_part))

def sort(left_, right_):
    res = []
    while len(left_) != 0 and len(right_) != 0:
        # do stuff
        if left_[0] > right_[0]:
            res.append(right_[0])
            right_.remove(right_[0])
        else:
            res.append(left_[0])
            left_.remove(left_[0])
    if len(right_) == 0:
        res = res + (left_)
    else:
        res = res + (right_)
    return res


def main():
    sample_list = [9, 81, 0, 0, 5, 7, 27, 12, 46]
    result = merge_sort(sample_list)
    print(result)



if __name__ == '__main__':
    main()

