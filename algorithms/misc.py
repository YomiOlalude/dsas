from collections import Counter


def add_up_to(n):
    """
    add_up_to(5) -> 5 + 4 + 3 + 2 + 1 = 15
    """
    return n * (n + 1) / 2


def print_pairs(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            print(arr[i], arr[j])


def has_matching_squares(arr1, arr2):
    """
    return true if every value in arr1 has its corresponding squared value in arr2,
    and frequency of values must be same
    """
    if len(arr1) != len(arr2):
        return False

    arr1_squared = list(map(lambda item: item**2, arr1))

    arr2.sort()
    arr1_squared.sort()

    if arr2 == arr1_squared:
        return True
    return False


def frequency_counter(iterable):
    result = {}

    for item in iterable:
        if item not in result:
            result[item] = 1
        else:
            result[item] += 1
    return result


def are_anagrams(string1, string2):
    string1_freq = Counter(string1)
    string2_freq = Counter(string2)

    if string1_freq == string2_freq:
        return True
    return False


def traverse_matrix(matrix):
    """
    [
      [1,2,3],
      [8,9,4],
      [7,6,5]
    ]
    -> [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    if not matrix or not matrix[0]:
        return []

    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result
