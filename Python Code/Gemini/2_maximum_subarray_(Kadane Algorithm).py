# Maximum Subarray (Kadane’s Algorithm): Find the sum of the contiguous subarray with the largest sum.
# Logic: Maintain `current_sum` and `max_so_far`. If `current_sum < 0`, reset it.


def maxSubArray(nums):
    # Initialize both with the first element
    max_so_far = nums[0]
    current_sum = nums[0]

    # Start from the second element
    for i in range(1, len(nums)): 
        # Decision: Start fresh at nums[i] or continue the old sum?
        current_sum = max(nums[i], current_sum + nums[i])

        # Keep trakc of the best we've ever seen
        max_so_far = max(max_so_far, current_sum)
    
    return max_so_far