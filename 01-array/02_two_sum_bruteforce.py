"""
Two Sum - Brute Force
=====================

Problem:
    Given a list of integers and a target, determine whether two
    different elements add up to the target.

Example:
    numbers = [2, 7, 11, 15]
    target = 9
    Output: True

Approach:
    Check every unique pair using two loops. The inner loop starts
    at i + 1 so an element is not paired with itself and pairs are
    not checked twice. Stop once a matching pair is found.
"""

numbers = [2, 7, 11, 15]
target = 9

found = False

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            found = True
            break

    if found:
        break

print(found)  # True


# Worst-case Time Complexity: O(n^2) - checks all unique pairs.
# Auxiliary Space Complexity: O(1) - uses a fixed number of variables.
