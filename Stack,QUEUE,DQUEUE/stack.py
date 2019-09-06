class Stack(object):

	def __init__(self):
		self.items=[]


	def push(self,data):
		self.items.append(data)
		print(data,"has pushed")

	def pop(self):
		self.items.pop()
		print("Poped")


	def isempty(self):
		print(len(self.items)==0)

	def peek(self):
		print(self.items[len(self.items)-1])

	def size(self):
		print(len(self.items))

	def display(self):
		print(self.items)




vinay = Stack()

vinay.push(2)
vinay.push(3)
vinay.push("Hello")
vinay.display()
vinay.pop()
vinay.isempty()
vinay.pop()
vinay.pop()
vinay.display()
vinay.isempty()

