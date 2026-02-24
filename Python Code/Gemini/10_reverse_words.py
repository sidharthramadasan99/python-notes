#10_reverse_words.py
#
#
#
#

def reverse_words(s):
    # .split() automatically handles multiple spaces
    words = s.split()
    return " ".join(words[::-1])