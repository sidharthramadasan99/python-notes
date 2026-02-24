# 
# 
# 
# 

from collections import Counter

def is_anagram(s,t):
    # Quick check: lengthes must match
    if len(s) != len(t):
        return False
    # Counter creates a frequency dictonary in one line
    return Counter(s) == Counter(t)