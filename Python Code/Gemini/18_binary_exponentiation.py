#18_binary_exponentiation.py
#
#
#

def myPow(x, n):
    if n < 0:
        x = 1/x
        n = -n
    res = 1
    while n:
        if n % 2: # If n is odd
            res *=x 
        x *=x 
        n //=2
    return res