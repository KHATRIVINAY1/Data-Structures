def pair(ls,k):
	arr=[]
	for i in range(len(ls)):
		for j in range(i+1,len(ls)):
			if ls[j]+ls[i]==k and not (ls[j],ls[i]) in arr:
				arr.append((ls[i],ls[j]))

	return arr

def pair_2(ls,k):
	seen =set()
	out=set()
	for num in ls:
		tar =k-num
		if tar not in seen:
			seen.add(num)
		else:
			out.add((num,tar))
	return out



print(pair([4,3,2,2,2],5))
print(pair_2([4,3,2,2,2],5))