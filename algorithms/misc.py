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


def permutation(arr):
    """
    return 'permutation' of arr in 2s
    [1,2,3,4] --> [(1,2), (1,3), (2,1), (2,3), (3,1), (3,2)]
    """
    result = []
    for num in arr:
        for i in range(len(arr)):
            if arr.index(num) != i:
                result.append([num, arr[i]])
    return result


def two_pointer_has_pair_with_sum(arr, target):
    """
    return True if array has 2 numbers that add up to target
    """
    left = 0
    right = len(arr) - 1
    result = False

    while left < right:
        total = arr[left] + arr[right]

        if total < target:
            left += 1
            continue
        elif total > target:
            right -= 1
            continue
        else:
            result = True
            return [arr[left], arr[right]]
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

    def safe_get(arr, index):
        try:
            return arr[index]
        except IndexError:
            return None

    if not matrix or not matrix[0]:
        return []

    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            result.append(safe_get(matrix[top], i))
        top += 1

        for i in range(top, bottom + 1):
            result.append(safe_get(matrix[i], right))
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(safe_get(matrix[bottom], i))
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(safe_get(matrix[i], left))
            left += 1
    return result


def rotate_matrix(matrix):
    length = len(matrix)
    for i in range(length):
        for j in range(i, length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix


def max_non_overlapping_intervals(intervals):
    """
    find the maximum number of non-overlapping intervals.
    max_non_overlapping_intervals([[1, 10], [0, 30], [15, 20]]) -> 2
    """
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[1])

    count = 0
    last_end_time = float("-inf")

    for start, end in intervals:
        if start >= last_end_time:
            count += 1
            last_end_time = end

    return count


class NumberToWords:
    """
    1234 returns 'One Thousand Thirty Four'
    """

    def __init__(self):
        self.units = {
            0: "Zero",
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
        }
        self.teens = {
            0: "Ten",
            1: "Eleven",
            2: "Twelve",
            3: "Thirteen",
            4: "Fourteen",
            5: "Fifteen",
            6: "Sixteen",
            7: "Seventeen",
            8: "Eighteen",
            9: "Nineteen",
        }
        self.tens = {
            0: "",
            1: "",
            2: "Twenty",
            3: "Thirty",
            4: "Forty",
            5: "Fifty",
            6: "Sixty",
            7: "Seventy",
            8: "Eighty",
            9: "Ninety",
        }
        self.thousands = ["", "Thousand", "Million", "Billion", "Trillion"]

    def number_to_words(self, num: int) -> str:
        num_is_negative = num < 0
        num = abs(num)

        if num == 0:
            return self.units[0]

        result = ""

        for i in range(len(self.thousands)):
            if num % 1000 != 0:
                result = self.helper(num % 1000) + self.thousands[i] + " " + result
            num = num // 1000
        return "Minus " + result.strip() if num_is_negative else result.strip()

    def helper(self, num: int) -> str:
        if num == 0:
            return ""
        elif num < 10:
            return self.units[num] + " "
        elif num < 20:
            return self.teens[num - 10] + " "
        elif num < 100:
            return self.tens[num // 10] + " " + self.helper(num % 10)
        else:
            return self.units[num // 100] + " Hundred " + self.helper(num % 100)


def return_max_overlapping_threads(threads):
    """
    returns the max possible number of concurrent threads
    [(1,4), (3,5), (2,7), (8,9)] --> 3
    """
    threads_list = []

    for thread in threads:
        for item in list(range(thread[0], thread[1] + 1)):
            threads_list.append(item)

    frequencies = Counter(threads_list)
    max_frequency = max(frequencies, key=frequencies.get)

    return frequencies[max_frequency] if frequencies[max_frequency] > 1 else 0
