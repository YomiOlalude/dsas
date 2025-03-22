def add_up_to(num):
    """
    add_up_to(5) -> 5 + 4 + 3 + 2 + 1 = 15
    """
    if num <= 0:
        return 0
    return num + add_up_to(num - 1)


def countdown(num):
    """
    countdown(5) -> 5 4 3 2 1 0
    """
    print(num)
    if num <= 0:
        return "Finished"
    return countdown(num - 1)


def factorial(num):
    """
    factorial(5) -> 5 * 4 * 3 * 2 * 1
    """
    if num == 0:
        return 0

    if num == 1:
        return 1

    return num * factorial(num - 1)


def fibonacci_array(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    result = fibonacci_array(n - 1)
    result.append(result[-1] + result[-2])
    return result


def fibonacci_add(n, memo=None):
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]
    if n <= 2:
        return 1

    memo[n] = fibonacci_add(n - 1, memo) + fibonacci_add(n - 2, memo)
    return memo[n]


def reverse_string(string):
    if len(string) <= 1:
        return string
    return string[-1] + reverse_string(string[:-1])


def flatten_array(arr):
    if not arr:
        return []

    if isinstance(arr[0], list):
        return flatten_array(arr[0]) + flatten_array(arr[1:])

    return [arr[0]] + flatten_array(arr[1:])
