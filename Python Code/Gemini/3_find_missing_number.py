# 
# 
# 
# 


def findMissingNumbers(nums):
    n = len(nums)
    # The range is 1 to n+1, so the 'total count' of numbers should be n+1
    total_elements = n+1

    # Mathematical sum of first 'total_elements' natural numbers
    expected_sum = (total_elements * (total_elements + 1))//2
    
    # Sum of elements present in the array
    actual_sum = sum(nums)

    return expected_sum - actual_sum