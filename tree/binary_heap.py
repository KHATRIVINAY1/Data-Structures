class Binary_Heap:
	
	def __init__(self):
		self.heaplist=[0]
		self.current_Size=0


	def up_heap(self,i):
		while i//2>0:
			if self.heaplist[i] < self.heaplist[i//2]:
				self.heaplist[i//2],self.heaplist[i]=self.heaplist[i],self.heaplist[i//2]
			i = i//2
		

	def insert(self,data):
		self.heaplist.append(data)
		self.current_Size+=1
		self.up_heap(self.current_Size)


	def down_heap(self,i):
		while(i*2)<=self.current_Size:
			mc= self.minchild(i)
			if self.heaplist[i]>self.heaplist[mc]:
				heaplist[i],heaplist[mc]=heaplist[mc],heaplist[i]

			i=mc

	def minchild(self,i):
		if i*2+1>self.current_Size:
			return i*2

		else:
			if self.heaplist[i*2]<self.heaplist[i*2+1]:
				return i*2

			else:
				return i*2+1

	def del_min(self):
		r = self.heaplist[1]
		self.heaplist[1]=self.heaplist[self.current_Size]
		self.current_Size-=1
		self.heaplist.pop()
		self.down_heap(1)
		return r
	
	def show(self):
		return self.heaplist[1:] 


heap_tree = Binary_Heap()
heap_tree.insert(100)
heap_tree.insert(200)
heap_tree.insert(300)
heap_tree.insert(700)
heap_tree.insert(20)

print(heap_tree.show())

