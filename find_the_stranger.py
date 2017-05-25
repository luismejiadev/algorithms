"""
You are given an array (which will have a length of at least 3,
but could be very large) containing integers.
The array is either entirely comprised of odd integers
or entirely comprised of even integers
except for a single integer N.
Write a method that takes the array as an argument and returns N.

For example:

[2, 4, 0, 100, 4, 11, 2602, 36]

Should return: 11
"""


def find_outlier(integers):
    sorted_list = sorted(integers, key=lambda v: v % 2)
    index = len(integers) - 1 if sorted_list[1] % 2 == 0 else 0
    return sorted_list[index]
