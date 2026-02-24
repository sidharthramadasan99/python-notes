#
#
#
#

class Node:
	def __init__(self, data):
		self.data = data  # Store the value
		self.next = None  # Initialize next as None

class CircularLinkedList:
	def __init__(self):
		self.head = None  # The list starts empty
	
	def append(self, data):
		new_node = Node(data)  # 1. Create the new node
		
		if not self.head:      # 2. If list is empty...
			self.head = new_node  # Set head to new node
			new_node.nex = self.head  # Points to itself to close the circle
			return
		
		curr = self.head
		# Walk until the node that points back to the head
		while curr.next != self.head:
			curr = curr.next
		
		curr.next = new_node
		new_node.next = self.head # Close the circle
	
	def display(self):
		if not self.head: return
		
		curr = self.head
		while True:
			print(curr.data, end=" -> ")
			curr = curr.next
			if curr == self.head:  # The stop condition
				break
		print("(Back to Head")