def nth(node,n):
	count=1
	ah=bh= node

	while ah.nextnode:
		if count < n:
			ah= ah.nextnode
			count +=1
		else:
			ah= ah.nextnode
			bh= bh.nextnode

	return (bh.data)	

def nth_to_last(head,n):
	left_pointer =head
	right_pointer=head
	for i in range(n-1):
		if not right_pointer.nextnode:
			raise LookupError("Error is large")

		else:
			right_pointer = right_pointer.nextnode

	while right_pointer.nextnode:
		left_pointer=left_pointer.nextnode
		right_pointer=right_pointer.nextnode

	return left_pointer.data



class Node():
	def __init__(self, data):
		self.data = data
		self.nextnode = None

a= Node(1)

b= Node(2)

c= Node(3)

d= Node(4)
e=Node(5)   

a.nextnode= b
b.nextnode=c
c.nextnode=d
d.nextnode=e

print(nth_to_last(a,0))
print(nth(a,0))