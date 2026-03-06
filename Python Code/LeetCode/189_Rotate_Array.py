# Leetcode 189
# Rotate Array
# 

def rotate(nums, k):
    n = len(nums)
    k %=n 

    # Slice the last k elements and first n-k elements
    # Then re-assign them to the original nums array
    nums[:] = nums[n-k:] + nums[:n-k]

    return nums