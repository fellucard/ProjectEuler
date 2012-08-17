# -- coding: UTF-8 --
__author__ = 'Mateusz'

def Problem3(number):
    tab = []
    startnumber = 2
    while (number > 1):
        while (number % startnumber == 0):
            tab.append(startnumber)
            number /= startnumber
        startnumber += 1
    return tab


print Problem3(600851475143)[-1]