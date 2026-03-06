

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # STandard dictionary
        anagram_map = {}

        for s in strs:
            # Step 1: Create the signature by sorting the string
            # Sorted ("eat") -> ['a','e','t'] -> join to "aet"
            key = "".join(sorted(s))

            # Step 2: Check if the key exists
            if key not in anagram_map:
                anagram_map[key] = []
            
            # Step 3: Append the original string
            anagram_map[key].append(s)
        
        # Step 4: Retrun the grouped lists
        return list(anagram_map.values())

s = Solution

print(s.groupAnagrams(s,["eat","tea","tan","ate","nat","bat"]))
print(s.groupAnagrams(s,[""]))
print(s.groupAnagrams(s,["a"]))

# Open terminal (ctrl+`). Run 'Python Code\LeetCode> python .\49_Group_Anagrams.py'