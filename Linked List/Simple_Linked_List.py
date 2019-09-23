class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None

class Linked_List():
	def __init__(self,head=None):
		self.head = head
		self.size= 0

	def append(self,data):

		if not self.head:
			self.new_node = Node(data)
			self.head  = self.new_node
			self.tail = self.new_node

		else:
			self.new_node= Node(data)
			self.tail.next = self.new_node
			self.tail= self.new_node

		self.size+=1

	def add_front(self,data):
		if not self.head:
			self.new_node = Node(data)
			self.head  = self.new_node
			self.tail = self.new_node
		else:
			self.new_node= Node(data)
			self.new_node.next= self.head
			self.head= self.new_node
		self.size+=1

	def add_mid(self,pos,data):
		self.temp = self.head
		self.count = 1
		

		if pos==1 or pos==0:
			self.add_front(data)
			return "front done"

		if pos >self.size:
			self.append(data)
			return "append done"
		self.new_node = Node(data) 

		while self.temp:
			self.count+=1
			if self.count==pos:
				p = self.temp.next 
				self.temp.next = self.new_node
				self.new_node.next=p
				break
			else:
				self.temp= self.temp.next
		self.size+=1

		return ' although done'



	def display(self):
		self.k = self.head

		while self.k:

			print(self.k.data)
			self.k= self.k.next


