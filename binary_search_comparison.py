# Binary search algorithms comparison

import time
import random


# https://www.geeksforgeeks.org/python-program-for-binary-search/
# Python 3 program for recursive binary search.
def recursive_binary_search(arr, x, low=0, high=None):
    # Check base case

    if high is None:
        high = len(arr) - 1

    if high >= low:

        mid = (high + low) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return recursive_binary_search(arr, x, low, mid - 1)

        # Else the element can only be present in right subarray
        else:
            return recursive_binary_search(arr, x, mid + 1, high)

    else:
        # Element is not present in the array
        return -1


# https://www.programiz.com/dsa/binary-search
def iterative_binary_search(array, x, low=0, high=None):

    if not high:
        high = len(array) - 1

    # Repeat until the pointers low and high meet each other
    while low <= high:

        mid = low + (high - low)//2

        if array[mid] == x:
            return mid

        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1


# https://www.geeksforgeeks.org/python-program-for-binary-search/
# Iterative Binary Search Function
def iterative_binary_search_2(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1

        # means x is present at mid
        else:
            return mid

    # If we reach here, then the element was not present
    return -1


def unconventional_binary_search(input_array, value):
    arr_len = len(input_array)
    indent = 0
    size = arr_len

    while size > 0:
        index = size // 2 + indent
        index_value = input_array[index]
        if index_value < value:
            indent = index+1
            size = arr_len - indent
        elif index_value > value:
            size //= 2
        else:
            return index
    return -1


def main():

    array_length = 31
    search_values_count = 10
    repetitions = 100000

    print("Binary search algorithms comparison\n")

    test_list = []
    new_n = 0
    for i in range(array_length):
        new_n += random.randint(1, 10)
        test_list.append(new_n)

    search_values = []
    for i in range(search_values_count):
        search_values.append(random.randint(-max(test_list)//2, max(test_list) + max(test_list)//2))

    functions = [recursive_binary_search, iterative_binary_search, iterative_binary_search_2, unconventional_binary_search]

    for f in functions:
        print(f"STARTED {f.__name__}. Array length is {len(test_list)}. {repetitions * len(search_values)} iterations")

        start = time.time()
        for i in range(repetitions):
            for n in search_values:
                f(test_list, n)

        end = time.time()
        print(f"{f.__name__}: Time elapsed: {end - start}\n")


if __name__ == "__main__":
    main()
