'''
address of array element = base + (cellsize)(index)
character in python occupy 16 bits =2 byte
'''
import sys
data=[]
n=10
for i in range(n):
	a=len(data)
	b=sys.getsizeof(data)
	print('Length: {0}; Size in bytes:{1}'.format(a,b))

	data.append(i)

