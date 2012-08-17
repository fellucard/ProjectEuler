"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
# -- coding: UTF-8 --
__author__ = 'Mateusz'


def problem4():
    notes = []
    for i in range(100, 999):
        for j in range(100, 999):
            string = i * j
            string = str(string)
            if string == string[::-1]:
                notes.append(i*j)
    return max(notes)


print problem4()
# Output: 906609