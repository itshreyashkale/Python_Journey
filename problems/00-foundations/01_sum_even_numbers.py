"""
Problem: Sum of Even Numbers

Given a list of integers, calculate the sum of only the even numbers.

Example:
    Input:  [3, 8, 12, 7, 5]
    Output: 20

Explanation:
    The even numbers are 8 and 12.
    Their sum is 8 + 12 = 20.

Pattern:
    Traversal + Filtering + Accumulator

Approach:
    1. Start a running total at 0.
    2. Visit each number once.
    3. Check whether number % 2 == 0.
    4. If it is even, add it to the running total.
    5. Print the total.
"""

numbers = [3, 8, 12, 7, 5]

total = 0

for number in numbers:
    if number % 2 == 0:
        total += number

print(total)  # Output: 20


# Time Complexity: O(n) - each list element is checked once.
# Auxiliary Space Complexity: O(1) - only a running total is used.
