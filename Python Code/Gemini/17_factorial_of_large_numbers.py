#17_factorial_of_large_numbers
#
#
#

def factorial(n):
    res = 1
    for i in range(2, n+1):
        res *= i
    return res