def intsplit(n):
	if n // 10 == 0:
		return n
	else:
		return n%10 + intsplit(n//10)


print(intsplit(4321))