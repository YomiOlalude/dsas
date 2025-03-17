def add_up_to(n):
    """
    add_up_to(5) -> 5 + 4 + 3 + 2 + 1 = 15
    """
    return n * (n + 1) / 2


def print_pairs(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            print(arr[i], arr[j])


def flatten_array(arr):
    if not arr:
        return []

    if type(arr[0]) is list:
        return flatten_array(arr[0]) + flatten_array(arr[1:])

    return [arr[0]] + flatten_array(arr[1:])
