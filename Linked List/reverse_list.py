
def reverse(head):
	current = head
	privious =None
	nextnode=None

	while current:
		nextnode=current.nextnode
		current.nextnode=privious
		privious=current

		current=nextnode

	return privious



class Node():
	def __init__(self, data):
		self.data = data
		self.nextnode = None

a= Node(1)

b= Node(2)

c= Node(3)

d= Node(4)

a.nextnode= b
b.nextnode=c
c.nextnode=d

print(a.nextnode.data)

print(b.nextnode.data)

print(c.nextnode.data)

reverse(a)


print(b.nextnode.data)

print(c.nextnode.data)
print(d.nextnode.data)