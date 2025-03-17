def linear_search(arr, target):
    for i in range(len(arr) - 1):
        if arr[i] == target:
            return i
    return -1


def binary_search(arr, num):
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = (right + left) // 2
        if arr[middle] == num:
            return middle

        if arr[middle] > num:
            right = middle

        if arr[middle] < num:
            left = middle

    return -1


def short_string_in_long_string(long, short):
    """
    Returns index of a short string in a long string
    """
    for _ in range(len(long)-1):
        for j in range(len(long)-2):
            if long[j] + long[j+1] + long[j+2] == short:
                return j
    return -1
