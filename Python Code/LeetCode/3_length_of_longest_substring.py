# Leetcode 3
# Lenth of Longest substring without repeating characters.
# 
# Logic: Slinding window problem
# 1. Initialize: Create a dictionary (hash map) to store the last seen index of each character and a start pointer for your window.
# 2. Expand: Use a for loop with a right pointer to iterate through the string.
# 3. Check for Duplicates: If the current character is already is your map, and its recorded index is within the current window (at or after start), move the start pointer to the index after the last seen position of that character.
# 4. Update: Store/update the current character's index in the map and calculate the current window length:
#   right - start + 1.
#   Update the maximum length found so far.

def lengthOfLongestSubstring(s: str) -> int:
    char_map = {}   # {character: last_seen_index}
    max_len = 0
    start = 0   # Left pointer of the window

    for right, char in enumerate(s):    # Note: enumerate() function in Python is used to loop over an iterable and get both the index and the element at the same time.
        if char in char_map and char_map[char] >= start:
            # Move the start to just after the previous occurance
            start = char_map[char] + 1
        
        # Always update the last seen index of the character
        char_map[char] = right

        # Calculate current window size and update max
        max_len = max(max_len, right -start + 1)
    
    return max_len

# Complexity Analysis
# - T C: O(n) - We traverse the string once.
# - S C: O(min(m,n)): m is the size of the character set