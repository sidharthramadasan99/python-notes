# 
# 
# 
# 

def moveZeros(nums):
    # Pointer for the position of the next non-zero element
    last_non_zero = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            # Swap elements
            nums[last_non_zero], nums[i] = nums[i], nums[last_non_zero]
            # Move the slow pointer forward
            last_non_zero += 1
        
        return nums