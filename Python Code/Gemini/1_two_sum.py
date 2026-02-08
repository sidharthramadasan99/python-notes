# Given an array and a target, find indices of two numbers that add up to the target.

# To solve the Two Sum problem efficiently, instead of checking every pair, we use a Hash Map (a dictonary in Python) to remember which numbers we have already seen as we traverse the array once.

def twoSum(nums, target): # e.g: (nums=[1,2,3,4,5,6], target=5)
    # Dictonary to store the value and its index
    # {numer: index}
    previousMap = {}

    for i, n in enumerate(nums):
        diff = target - n   
        
        # Check if the needed number exists in our 'history'
        if diff in previousMap:
            return [previousMap[diff], i]
        
        # Store the current number and its index for future reference
        previousMap[n] = i

    return [] # Should not happen based on problem constraints


