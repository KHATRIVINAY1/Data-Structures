def selectioonsort(arr):
	for i in range(len(arr)-1,0,-1):
		maxi = 0
		for j in range(1,i+1):
			if arr[j]>arr[maxi]:
				maxi=j
		arr[i],arr[maxi]=arr[maxi],arr[i]

	return arr


print(selectioonsort([26,54,93,17,77,31,44,55,20]))




