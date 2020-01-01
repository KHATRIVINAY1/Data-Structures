def quick_sort(arr):
	quick_sort_invoke(arr,0,len(arr)-1)

def quick_sort_invoke(arr,f,l):
	if f<l:
		splitpoint = partition(arr,f,l)

		quick_sort_invoke(arr,f,splitpoint-1)
		quick_sort_invoke(arr,splitpoint+1,l)

def partition(arr,f,l):
	pivot = arr[f]

	left = f+1
	right =l

	done= False

	while not done:
		while left<=right and arr[left]<=pivot:
			left+=1

		while arr[right]>=pivot and right>=left:
			right -= 1

		if right<left:
			done=True
		else:
			temp = arr[left]
			arr[left]=arr[right]
			arr[right]=temp


	temp=arr[f]
	arr[f]=arr[right]
	arr[right]=temp

	return right

arr = [2,5,6,7,12,23,5,56]
quick_sort(arr)
print(arr)