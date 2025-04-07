# Notes:
"""
1. The best case Big O for any sort algorithm is O (nlog n)
"""


def bubble_sort(arr):
    """
    Repeatedly swaps adjacent elements if they are in the wrong order,
    making larger elements "bubble" to the end
    """
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


def selection_sort(arr):
    """
    Repeatedly selects the smallest element from the unsorted part
    and swaps it with the first unsorted element
    """
    for i in range(len(arr)):
        lowest = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[lowest]:
                lowest = j
        arr[i], arr[lowest] = arr[lowest], arr[i]
    return arr


def insertion_sort(arr):
    """
    Builds a sorted array by picking one element at a time
    and inserting it into its correct position
    """
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = current
    return arr


def merge_sort(arr):
    """
    Recursively splits the array in half, sorts each half,
    and merges them back together in order
    """

    def merge(arr1, arr2):
        results = []
        i = 0
        j = 0

        while i < len(arr1) and j < len(arr2):
            if arr2[j] > arr1[i]:
                results.append(arr1[i])
                i += 1
            else:
                results.append(arr2[j])
                j += 1

        if i < len(arr1):
            results.extend(arr1[i:])

        if j < len(arr2):
            results.extend(arr2[j:])
        return results

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)
