class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None

class Linked_List():
	def __init__(self,head=None):
		self.head = head

	def append(self,data):

		if not self.head:
			self.new_node = Node(data)
			self.head  = self.new_node
			self.tail = self.new_node

		else:
			self.new_node= Node(data)
			self.tail.next = self.new_node
			self.tail= self.new_node

	
	def display(self):
		self.k = self.head

		while self.k:

			print(self.k.data)
			self.k= self.k.next


