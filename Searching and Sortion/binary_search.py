# def binary_search(arr,ele):
# 	f = 0
# 	l = len(arr)-1
# 	mid = l//2
# 	found=False
# 	while f <= l and not found:
# 		mid =(f+l)//2
# 		if arr[mid]==ele:
# 			found=True
# 		else:
# 			if ele <arr[mid]:
# 				l =mid-1
# 			else:
# 				f=mid+1
# 	return found


# print(binary_search([1,2,3,4,5],12))

def binary(arr,ele):

	if len(arr)==0:
		return False
	else:
		mid =len(arr)//2
		if arr[mid]==ele:
			return "Found element"
		else: 
			if arr[mid] > ele:
				return binary(arr[:mid],ele)
			else:
				return binary(arr[mid+1:],ele)


print(binary([1,2,3,4,5],1))
