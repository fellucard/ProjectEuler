"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
# -- coding: UTF-8 --
__author__ = 'Mateusz'


def problem3(number):
    tab = []
    startnumber = 2
    while number > 1:
        while (number % startnumber == 0):
            tab.append(startnumber)
            number /= startnumber
        startnumber += 1
    return tab[-1]

print problem3(600851475143)
# Output: 6857