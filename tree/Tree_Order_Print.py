import collections
def level(tree):
	if not tree:
		return
	node =collections.deque([tree])
	currentCount =1
	nextcount =0
	while len(node)!=0:
		currentNode = node.popleft()
		currentCount-=1
		print(currentNode.value)

		if currentNode.left:
			node.append(currentNode.left)
			nextcount+=1

		if currentNode.right:
			node.append(currentNode.right)
			nextcount+=1

		if currentCount==0:
			print('\n')
			currentCount,nextcount= nextcount,currentCount


 class Node():
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.right= right
        self.left=left

root = Node(10) 
root.left = Node(20)
root.right = Node(30)


level(root)