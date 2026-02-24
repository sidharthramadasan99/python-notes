#
#
#
#

def compress(chars):
    i = 0 # Read pointer
    res = 0 # Write pointer
    while i < len(chars):
        char = chars[i]
        count = 0
        while i < len(chars) and chars[i] == char:
            count += 1
            i += 1
        chars[res] = char
        res += 1
        if count > 1:
            for digit in str(count):
                chars[res] = digit
                res += 1
    return res