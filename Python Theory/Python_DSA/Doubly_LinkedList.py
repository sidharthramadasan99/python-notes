#
#
#
#

class Node:
    def __init__(self,data):
        self.data = data  # Stores the actual value
        self.next = None  # Pointer to the next node. None is a special constant used to represent the absence of a value or a null value.
        self.prev = None  # Pointer to the previous node.

class DoublyLinkedList:
    def __init__(self):
        self.head = None  # The starting point to the list

    def append(self, data):
        new_node = Node(data)
        if not self.head:  # If list is empty, new node becomes the head
            self.head = new_node 
            return
        
        last = self.head
        while last.next: # Traverse to the end of the list
            last = last.next
        
        last.next = new_node  # Link the old last node to the new node
        new_node.prev = last  # Link the new node back to the old last node

    def prepend(self, data):
        """Add a node to the beginning of the list."""
        new_node = Node(data)
        if self.head:
            self.head.prev = new_node # Link current head back to the new node
            new_node.next = self.head # LInk new node forward to current head
        self.head = new_node          # Move the head pointer to the new node
    
    def delete(self, key):
        """Delete the first occurance of a node with the given value."""
        curr = self.head

        while curr:
            if curr.data == key:
                if curr.prev:  # IF no the head node
                    curr.prev.next = curr.next
                else:
                    self.head  = curr.next
                
                if curr.next: # IF not the last node
                    curr.next.prev = curr.prev
                
                curr = None
                return
            curr = curr.next
        
        def display_forward(self):
            """Print all nodes from head to tail."""
            curr = self.head
            while curr:
                print(curr.data, ends=" <-> ")
            print("None")

# """
# Efficiency trade-offs

# | Operation          | Complexity | Note                                                          |
# | ------------------ | ---------- | ------------------------------------------------------------- |
# | Access/Search      | O(n)       | Must traverse linearly.                                       |
# | Insertion(at ends) | O(1)       | If you maintain a tail pointer(this code is O(n) without one) |
# | Deletion           | O(n)       | O(1) if you already have a reference to the node.             |

# """
                
