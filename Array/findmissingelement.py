import collections

def finder(arr1,arr2):
	arr2.sort()
	arr1.sort()

	for num1,num2 in zip(arr1,arr2):
		if num2 != num1:
			return num1

	return arr1[-1]

def finder2(arr1,arr2):
	d =collections.defaultdict(int)

	for num in arr2:
		d[num]+=1

	for num in arr1:
		if d[num]==0:
			return num
		else:
			d[num]=-1


print(finder([1,2,3,4,5],[2,3,1,4,4]))
print(finder2([1,2,3,4,5],[2,3,1,4,4]))
