def cycle_check(node):
	marker1=node
	marker2 = node

	while marker2!=None and marker2.nextnode !=None:
		marker1 =marker1.nextnode
		marker2 = marker2.nextnode.nextnode

		if marker2==marker1:
			return True

	return False

def cycle(node):
	head = node
	nex= node.nextnode
	while nex.nextnode !=None:
		if nex == head:
			return True
		nex = nex.nextnode
	return False 


class Node(object):
	def __init__(self, data):
		self.data = data
		self.nextnode = None


a = Node(1)
b= Node(2)
c= Node(3)
a.nextnode=b
b.nextnode=c
c.nextnode=a



x = Node(1)
y= Node(2)
z= Node(3)
x.nextnode=y
y.nextnode=z


print(cycle(a))
print(cycle(x))