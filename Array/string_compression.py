def str_com(s):
	k= dict()

	for i in s:
		if i in k:
			k[i]+=1
		else:
			k[i]=1
	
	stri =""
	for i,j in k.items():
		stri+=str(i)+str(j)

	return stri

def compress(s):
	r = ''
	l = len(s)
	if l == 0:
		return " "

	if l ==1:
		return s+"1"


	last =s[0]
	cnt = 1
	i=1

	while i<l:
		if s[i] ==s[i-1]:
			cnt+=1
		else:
			r=r +s[i-1]+str(cnt)
			cnt =1

		i+=1

	r= r+s[i-1]+str(cnt)
	return r

print(str_com("AAaaa  "))
print(compress("AAbCCC"))