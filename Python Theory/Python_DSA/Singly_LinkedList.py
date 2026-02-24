#
#
#
#

class Node:
	def __init__(self, data):
		self.data = data  # Assign data to the node
		self.next = None  # Initialize next as null (no link yet)

class SinglyLinkedList:
	def __init__(self):
		self.head = None  # Initialize the list with an empty head
	
	def insert_at_end(self, data):
		"""Append a new node to the tail of the list."""
		new_node = Node(data)
		if not self.head():  # If list is empty, make new node the head
			self.head = new_node
			return
		
		last = self.head  # Start at the head
		while last.next:  # Traverse until the last node (where next is None)
			last = last.next
		
		last.next = new_node  # Link the old last node to the new node
	
	def delete_node(self, key):
		"""Remove the first node containing the specified data."""
		temp = self.head
		
		# Case 1: If the head node itself holds the key
		if temp and temp.data == key:
			self.head = temp.next  # Move head to the second node
			temp = None
			return
		
		# Case 2: Serach for the key while keeping track of the previous node
		prev = None
		while temp and temp.data != key:
			prev = temp
			temp = temp.next
		
		# If key was not present in the list
		if temp is None:
			return
		
		# Unlike the node from the linked list
		prev.next = temp.next
		temp = None
	
	def display(self):
		"""Print the list elements in order."""
		current = self.head
		while current:
			print(current.data, end=" -> ")
			current = current.next
		print("None")
