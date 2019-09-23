def Binary_Tree(data):
	return [data,[],[]]

def insert_right(root,data):
	t = root.pop(2)

	if len(root) > 1:
		root.insert(2,[data,[],t])

	else:
		root.insert(2,[data,[],[]])

	return root


def insert_left(root,data):
	t = root.pop(1)

	if len(root) > 1:
		root.insert(1,[data,t,[]])

	else:
		root.insert(1,[data,[],[]])

	return root

def get_root(root):
	return root[0]

def set_root(root,data):
	root[0]=data

def get_left_child(root):
	return root[1]

def get_right_child(root):
	return root[2]


