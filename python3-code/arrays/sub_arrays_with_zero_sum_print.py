from typing import List


def find_zero_sum_sub_arrays_naive(arr: List[int]) -> List[List[int]]:
    length = len(arr)
    if length == 0:
        return []
    if length == 1:
        return [[0]] if arr[0] == 0 else []

    result = list()

    for i in range(length):
        sm = 0
        for j in range(i, length):
            sm = sm + arr[j]
            if sm == 0:
                result.append(arr[i:j+1])

    return result


def find_zero_sum_sub_arrays_optimised(arr: List[int]) -> List[List[int]]:
    length = len(arr)
    if length == 0:
        return []
    if length == 1:
        return [[0]] if arr[0] == 0 else []

    result = list()

    mmap = dict()
    sm = 0
    for i in range(length):
        sm = sm + arr[i]
        if sm not in mmap:
            mmap[sm] = []
        mmap[sm].append(i)

    for k in mmap:
        v = mmap[k]
        if k == 0:
            for idx in v:
                result.append(arr[0:idx+1])
        lt = len(v)
        for i in range(1, lt):
            result.append(arr[v[i-1]+1:v[i]+1])
    return result


if __name__ == '__main__':
    print(find_zero_sum_sub_arrays_optimised([3, 4, -7, 3, 1, 3, 1, -4, -2, -2]))