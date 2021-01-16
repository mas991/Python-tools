
def count_numbers_in_array(a: list) -> list:
    """
    Counts the number of numbers present in the array and generates a new array with the result.
    Input: array of numbers.
    Output: Array of the results of counting each number from the input array.

    Example:
    [0, 1, 3, 0, 2, 2, 0] -> [3, 1, 2, 1]
    """
    a.sort()
    b = [0 for _ in range(a[-1]+1)]

    for i in range(len(a)):
        b[a[i]] += 1

    return b
