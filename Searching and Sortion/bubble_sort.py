def bubble_sort(arr):
	k = len(arr)

	for i in range(k):
		for p in range(k-1):
			if arr[p]> arr[p+1]:
				arr[p],arr[p+1]=arr[p+1],arr[p]
		k-=1

	return arr

print(bubble_sort([7,6,5,4,3,2,1]))
