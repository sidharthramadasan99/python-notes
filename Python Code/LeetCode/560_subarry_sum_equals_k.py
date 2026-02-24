# Leetcode 560
# Subarray Sum Equals K
# 
# Logic: Prefix Sum + Hash Map
# A Prefix Sum is the sum of all elements from the start of the array up to a certain index.
# If the sum from index 0 to i is Si, and the sum from 0 to j is Sj, then the sum of the subarray between i+1 and j is:
#     Subarray Sum = Sj - Si
# We want this difference to equal k. Therefore, we look for:Sj - k = Si
# 1. As you itterate keep a running total (current_sum)
# 2. Check if current_sum - k has been seen before in your hash map
# 3. If it has, it means there is a subarray ending at the current position that sums to k. Add the frequency of that prefix sum to your count.Update the hash map with the new current_sum.
# 
# 
# 


def subarraySum(nums, k):
    # count: total subarrays found
    # current_sum: running prefix sum
    count = 0
    current_sum = 0

    # prefix_sums: {sum_value: frequencey}
    # Initialize with 0:1 to handle subarrays starting from index 0
    prefix_sum = {0, 1}

    for n in nums:
        current_sum += n

        diff = current_sum - k 
        if diff in prefix_sum:
                count += prefix_sum[diff]
        
        # Record this current_sum in the map
        prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1

    return count 

