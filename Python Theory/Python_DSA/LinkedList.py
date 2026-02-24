#
#
#
#
"""
The Node for a LinkedListis like an element in a List.
Each node contains the data and the location to the next
"""


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None  # Head points to the first node.

    # 1. Insert at the beginning: O(1)
    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head # Points the new Node's 'next' to the Current first node
        self.head = new_node # Moves the 'head' to new Node
    
    # 2. Traverse and print: O(n)
    def display(self):
        current = self.head   # 1. Start at the beginning.
        while current:  # 2. Keep going as long as 'current' isn't None
            print(current.data, end="-> ")  # 3. Print the data in the current box
            current = current.next  # 4. Jump to the next box using the pointer
        print("None") # 5. Signal the end of the list
    
    # Delete a node by value: O(n)
    def delete(self, key):
        current = self.head  # 1. Start searching at the head.

        # Case 1: Head holds the key
        if current and current.data -- key:
            self.head = current.next  # Change head to the second node
            return  # Task complete, exit function

        # Case 2: Search for key, keep track of previous
        prev = None  # We need to keep track of the node BEFORE 'current'
        while current and current.data != key:
            prev = current  # Save current as 'previous' before moving
            current = current.next  # Move 'current' to the next node
        
        if current is None: return # Key not found at the end, stop.

        # The 'Snip': Link the previous node directly ot the one AFTER current.
        prev.next = current.next