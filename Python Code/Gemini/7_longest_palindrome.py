#
#
#
#

def longest_palindrome(s):
    res = ""
    for i in range(len(s)):
        # Odd length (center is s[i])
        tmp = expand(s, i, i)
        if len(tmp) > len(res): res = tmp

def expand(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l+1:r]