
### **Category 1: Arrays & Optimization**

1. **Two Sum:** Given an array and a target, find indices of two numbers that add up to the target.
* *Logic:* Use a Hash Map to store seen values. Time: , Space: .


2. **Maximum Subarray (Kadane’s Algorithm):** Find the sum of the contiguous subarray with the largest sum.
* *Logic:* Maintain `current_sum` and `max_so_far`. If `current_sum < 0`, reset it.


3. **Find the Missing Number:** Find the missing number in an array of size  containing numbers  to .
* *Logic:* Sum of first  natural numbers . Result is .


4. **Move Zeroes:** Move all 0s to the end of an array without changing the order of non-zero elements.
* *Logic:* Two-pointer approach. Swap non-zero elements to the "slow" pointer.


5. **Merge Sorted Arrays:** Merge two sorted arrays without using extra space (or in ).
* *Logic:* Use three pointers starting from the end of the arrays.



### **Category 2: Strings & Hashing**

6. **Valid Anagram:** Check if two strings contain the same characters.
* *Logic:* Use a frequency array (size 26) or a Hash Map.


7. **Longest Palindromic Substring:** Find the longest substring that reads the same backward.
* *Logic:* Expand around center for each character ().


8. **First Non-repeating Character:** Return the index of the first unique character in a string.
* *Logic:* Frequency map first pass; find first char with count 1 in second pass.


9. **String Compression:** "aaabbc"  "a3b2c1".
* *Logic:* Iterate and count consecutive occurrences. Handle edge cases where compressed length is not shorter.


10. **Reverse Words in a String:** "sky is blue"  "blue is sky".
* *Logic:* Split by space, reverse the list, and join.



### **Category 3: Basic Data Structures (Linked Lists & Stacks)**

11. **Reverse a Linked List:** Change the direction of pointers in a singly linked list.
* *Logic:* Iterative approach using `prev`, `curr`, and `next` pointers.


12. **Detect Cycle in Linked List (Floyd’s Cycle):** Check if a list has a loop.
* *Logic:* Slow and Fast pointers. If they meet, there is a cycle.


13. **Valid Parentheses:** Check if brackets `()[]{}` are closed in correct order.
* *Logic:* Use a Stack. Push opening; pop on closing and check match.


14. **Implement Queue using Stacks:** Use two stacks to simulate FIFO behavior.
* *Logic:* `Stack1` for push; `Stack2` for pop (transfer from `Stack1` when empty).



### **Category 4: Mathematical & Search/Sort**

15. **Binary Search:** Find an element in a sorted array.
* *Logic:* Repeatedly divide the search interval in half ().


16. **Nth Fibonacci Number:** Calculate Fibonacci efficiently.
* *Logic:* Use Iteration (Dynamic Programming) instead of recursion to avoid .


17. **Factorial of a Large Number:** Find factorial of 100+.
* *Logic:* Use an array/list to store digits since standard integers will overflow.


18. **Power(x, n):** Calculate  raised to .
* *Logic:* Use Binary Exponentiation () to prevent timeout.


19. **Sort an array of 0s, 1s, and 2s (Dutch National Flag):**
* *Logic:* Three pointers: `low`, `mid`, and `high`.


20. **Search in a 2D Matrix:** Efficiently find a value in a sorted matrix.
* *Logic:* Treat the matrix as a flattened 1D array and apply Binary Search.



---

