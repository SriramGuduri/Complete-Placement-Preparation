from typing import List


def sort_binary_array(arr: List[int]):
    num_of_1s = 0
    for num in arr:
        num_of_1s = num_of_1s + num
    num_of_0s = len(arr) - num_of_1s
    for i in range(num_of_0s):
        arr[i] = 0

    for i in range(num_of_0s, len(arr)):
        arr[i] = 1


if __name__ == '__main__':
    a = [1, 0, 1, 1, 0, 0, 0, 1]
    sort_binary_array(a)
    print(a)