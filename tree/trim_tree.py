def trimbt(tree,minval,maxval):
	if not tree:
		return
	tree.left = trimbt(tree.left,minval,maxval)
	tree.right=trimbt(tree.right,minval,maxval)

	if minval<= tree.val <=maxval:
		return tree

	if tree.val<minval:
		return tree.right

	if tree.val > maxval:
		return tree.right
		