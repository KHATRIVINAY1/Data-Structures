def unique(s):
	d= dict()
	i=0
	for i in s:
		if i in d:
			return False
		else:
			d[i]=1
	
	return True

def unique_2(s):
	return len(set(s)) == len(s)
print(unique(" abcd "))
print(unique_2(" abcd "))