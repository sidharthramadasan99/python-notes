# 128. Longest Consequtive Sequence
# 
# 
# OPTIMIZATION REQUIRED


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        
        numSet = set(nums)
        longest = 0

        for n in nums:
            if (n-1) not in numSet:
                length = 1

                c_num = n
                while (c_num+1) in numSet:
                    length += 1
                    c_num+=1
            longest = max(longest, length)

        return longest