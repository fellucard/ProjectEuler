"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
# -- coding: UTF-8 --
__author__ = 'Mateusz'


def problem5():
    """
    http://www.funtrivia.com/askft/Question79947.html
    """
    def gcd(first, second):
        """
        http://en.wikipedia.org/wiki/Greatest_common_divisor
        """
        return first if second == 0 else gcd(second, first % second)

    def lcm(first, second):
        """
        http://en.wikipedia.org/wiki/Least_common_multiple
        """
        return (first * second) / gcd(first, second)

    return reduce(lcm, range(2, 21))

print problem5()

# Output: 232792560

# Bruteforce
#
#table = range(1, 21)
#tabele = range(1, 300000000)
#
#for a in tabele:
#    n = 1
#    for i in table:
#        if n == 20:
#            print "NUMER: %d" % a
#        elif a % i == 0:
#            n += 1
#        else:
#            break
