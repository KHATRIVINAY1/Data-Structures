def arr_search(arr ,ele):
	'''  for ordered array'''
	for i in range(len(arr)):
		if arr[i]==ele:
			return i+1
		if arr[i] > ele:
			return None 
	return None


print(arr_search([1,2,3,4,5,7,8,9,10],7))
