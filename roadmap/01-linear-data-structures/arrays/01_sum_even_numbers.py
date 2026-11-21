"""
Sum of Even Numbers
===================

Problem:
    Given a list of integers, return the sum of all even numbers.

Example:
    Input:  [3, 8, 12, 7, 5]
    Output: 20

    The even values are 8 and 12, and their sum is 20.

Approach:
    Traverse the list once. Add a value to the running total only
    when it is divisible by 2.

Complexity:
    Time:  O(n) - each element is checked once.
    Space: O(1) - the algorithm uses a fixed amount of extra memory.
"""


def sum_even_numbers(numbers: list[int]) -> int:
    """Return the sum of the even values in numbers."""
    total = 0

    for number in numbers:
        if number % 2 == 0:
            total += number

    return total


if __name__ == "__main__":
    sample_numbers = [3, 8, 12, 7, 5]
    print(sum_even_numbers(sample_numbers))  # 20
