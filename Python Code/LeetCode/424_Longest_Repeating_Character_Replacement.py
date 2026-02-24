# Leetcode 424
# Longest Repeating Charcter Replacement
# 
# Logic: Advanced Slinding Window
# Window validity
# - Total characters in the window = right - left + 1
# - Most frequent characters count = max_freq
# - Characters to replace = (Total) - (max_freq)
# 
# (Total) - (max_freq) > k , the window is invalid. We must shrink it from the left.

def characterReplacement(s: str, k: int) -> int:
    count = {} # Frequency map for characters in the current window
    max_len = 0
    max_freq = 0
    left = 0

    for right in range(len(s)):
        # 1. Update frequency of the incoming character
        count[s[right]] = 1 + count.get(s[right], 0)

        # 2. Update the most frequent character count in the current window
        max_freq = max(max_freq, count[s[right]])

        # 3. If (window_size - max_freq) > k, the window is invalid
        while (right - left + 1) - max_freq > k:
            count[s[left]] -= 1
            left += 1
        
        # 4. Update the result
        max_len = max(max_len, right - left + 1)
    
    
    
    return max_len 

