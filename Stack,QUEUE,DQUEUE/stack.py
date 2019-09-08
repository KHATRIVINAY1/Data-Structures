class Stack(object):

	def __init__(self,size):
		self.items=[]
		self.size =size


	def push(self,data):
		if len(self.items) < self.size: 
			self.items.append(data)
			print(data,"has pushed")
		else:
			print("Stack is full")


	def pop(self):
		self.items.pop()
		print("Element has been poped")


	def isempty(self):
		print(len(self.items)==0)

	def isfull(self):
		print(len(self.items) ==self.size)

	def peek(self):
		print(self.items[len(self.items)-1])


	def display(self):
		for i in self.items[::-1]:
			print("|****|")
			print("|",i,"|")
		

size = int(input("How many elemtns you want to enter in your stack"))
stack = Stack(size)

stack.push(10)
stack.push(30)
stack.push(22)
stack.pop()
stack.display()
stack.isfull()
