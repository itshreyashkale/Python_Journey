# Problem: Sum of all even numbers in a list

numbers = [3, 8, 12, 7, 5]

total = 0

for number in numbers:
    if number % 2 == 0:
        total += number

print(total)  # Output: 20


# Pattern: Traversal + Filtering + Accumulator
# Time Complexity: O(n) - each element is checked once.
# Auxiliary Space Complexity: O(1) - only one running total is stored.
