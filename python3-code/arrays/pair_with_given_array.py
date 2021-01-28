from typing import List


def get_pair_with_sum(array: List[int], target: int):
    length = len(array)
    if length < 2:
        return None
    array.sort()
    left, right = 0, length-1
    while left < right:
        sm = array[left] + array[right]
        if sm == target:
            return (array[left], array[right])
        elif sm < target:
            left = left+1
        else:
            right = right-1
    return None


if __name__ == '__main__':
    arr = [8, 7, 2, 5, 3, 1]
    target = 10
    print(get_pair_with_sum(arr, target))