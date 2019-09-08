class Queue():
	
	def __init__(self):
		self.items = []

	def is_empty(self):
		if self.items == []:
			print("Queue is Empty")
		else:
			print("There are some elemetns in the Queue")

	def en_queue(self,data):
		self.items.insert(0,data)
		print(data,"has been added to the rear part of the Queue")

	def de_queue(self):
		self.items.pop()
		print("Front element of the Queue has been deleted")

	def size(self):
		print("The size of the Queue is:",len(self.items))

	def peek(self):
		print("The current Front element is:", self.items[len(self.items)-1])

	def show_queue(self):
		print("rear-->|",end="")
		for i in self.items:
			print(str(i)+"|",end="")
		print("<--Front")


q = Queue()
q.is_empty()
q.en_queue(4)
q.en_queue(10)
q.de_queue()
q.en_queue(12)
q.en_queue(13)
q.en_queue(14)