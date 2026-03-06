# Leetcode 23
# Container with most water
# 
# Logic:
# THe "Greedy" Two-pointer strategy
# Find two vertical lines on a graph that together with the x-axis, form a container that holds the most water
# 
# The amount of water is determined by two factors
# 1. Width: The distance between the two lines
# 2. Height: The height of the shorter of the two lines (because water overflows the shorted side)
# 
# Area = Width x min(Height1, Height2)
# - Checking every pair of lines is too slow. Instaed, we use a strategy that starts with the maximum possible width and then tries to find a better height.
# 1. Start width: Place one pointer at the very beginning (left) and one at the very end (right)
# 2. Calculate Area: Find the area between these two lines.
# 3. Move the "weak link": To find a larger area, you must find a taller line. Since the hieght is limited by the shorter line, moving the pointer of the taller line will only decrease the width without any chance of increasing the height. Therefore, you always move the pointer to the shorter line.
# 4. Repeat: Keep moving inward until the pointers meet.

def maxArea(height):
    max_val = 0
    left = 0                  # Left most index
    right = len(height) - 1   # Right most index

    while left < right:
        # Calculate current area
            width = right - left
            current_height = min(height[left], height[right])
            current_area = width * current_height

            # Update max if current is better
            max_val = max(max_val, current_area)

            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                  left += 1
            else:
                  right -= 1
    
    return max_val