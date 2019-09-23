def revers(s,count,st=''):
	
	if count==0:
		return s[count]

	else:
		st=s[count]
		return st + revers(s,count-1,st)

def reverse(s):
	if len(s)==1:
		return s
	else:
		return reverse(s[1:]) + s[0]
k="Hello World"
print(revers(k,len(k)-1))    