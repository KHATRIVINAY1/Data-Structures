class DoublyLinkedList():
	def __init__(self,value):
		self.value = value
		self.next_node = None 
		self.prev_node = None


a = DoublyLinkedList(1)

c = DoublyLinkedList(2)
b = DoublyLinkedList(3)

a.next_node=b
b.prev_node=a
b.next_node=c
c.prev_node=b