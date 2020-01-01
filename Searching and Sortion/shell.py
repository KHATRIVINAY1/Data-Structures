def shell_sort(arr):
	sublist_count =len(arr)//2
	while sublist_count > 0:
		for start in range(sublist_count):
			gap_insertion_sort(arr,start,sublist_count)

		sublist_count =sublist_count//2

	print(arr)


def gap_insertion_sort(arr,start,gap):
	for i in range(start+gap,len(arr),gap):
		currentvalue =arr[i]
		pos = i

		while pos > 0 and arr[pos-gap]> currentvalue:
			arr[pos]=arr[pos-gap]
			pos=pos - gap

		arr[pos]=currentvalue


shell_sort([45,67,23,45,21,24,7,2,6,4,90])