"""
Sum of Even Numbers
===================

Problem:
    Given a list of integers, calculate the sum of all even numbers.

Example:
    Input:  [3, 8, 12, 7, 5]
    Output: 20

Explanation:
    The even values are 8 and 12. Their sum is 20.

Approach:
    Traverse the list once. Add a number to the running total only
    when number % 2 == 0.

Complexity:
    Time:  O(n) - each element is checked once.
    Space: O(1) - only a running total is maintained.
"""


def sum_even_numbers(numbers: list[int]) -> int:
    """Return the sum of all even values in the list."""
    total = 0

    for number in numbers:
        if number % 2 == 0:
            total += number

    return total


if __name__ == "__main__":
    values = [3, 8, 12, 7, 5]
    print(sum_even_numbers(values))  # 20
