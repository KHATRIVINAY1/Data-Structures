class Binary_Tree():
	def __init__(self,rootobj):
		self.data = rootobj
		self.left = None
		self.right=None

	def insert_left(self,data):
		if self.left==None:
			self.left = Binary_Tree(data)
		else:
			t= Binary_Tree(data)
			t.left = self.left
			self.left =t

	def insert_right(self,data):
		if self.right==None:
			self.right = Binary_Tree(data)

		else:
			t= Binary_Tree(data)
			t.right =self.right
			self.left=t


	def get_root(self):
		return self.data

	def set_root(self,data):
		self.data= data


	def get_right(self):
		return self.right

	def get_left(self):
		return self.left