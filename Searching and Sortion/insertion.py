def insert_sort(arr):
	
	for i in range(1,len( arr)):
		temp=arr[i]
		pos=i
		while pos >0 and arr[pos-1]>temp:
			arr[pos] = arr[pos-1]
			pos-=1
		arr[pos] = temp


	print(arr)


insert_sort([54,26,93,17,77,31,44,55,20])
