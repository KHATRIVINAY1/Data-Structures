class Dequeue():
	def __init__(self):
		self.items = []

	def add_front(self,data):
		self.items.append(data)

	def add_rear(self,data):
		self.items.insert(0,data)

	def remove_front(self):
		self.items.pop()

	def remove_rear(self):
		self.items.pop(0)

	def is_empty(self):
		print(self.items==[])

	def size(self):
		print(len(self.items))

	def display(self):
		print("rear-->|",end="")

		for i in self.items:
			print(str(i)+"|",end="")

		print("<--Front")


d = Dequeue()
d.size()
d.display()
d.add_rear(10)
d.add_rear(11)
d.add_rear(12)
d.add_rear(13)
d.add_rear(14)
d.add_front(15)
d.size()
d.display()

d.remove_rear()
d.remove_rear()
d.size()
d.display()
