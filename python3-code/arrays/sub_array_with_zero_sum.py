from typing import List


def sub_array_with_zero_sum(arr: List[int]) -> bool:
    memory = set()
    memory.add(0)
    sm = 0
    for num in arr:
        sm = sm + num
        if sm in memory:
            return True
        memory.add(sm)
    return False


if __name__ == '__main__':
    print(sub_array_with_zero_sum([4, -6, 3, -1, 4, 2, 7]))
