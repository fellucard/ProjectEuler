"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""
# -- coding: UTF-8 --
__author__ = 'Mateusz'


def problem1(endrage):
    sume = 0
    for i in range(1, endrage):
        if i % 3 == 0 or i % 5 == 0:
            sume += i
    return sume

print problem1(1000)
# Output: 233168
