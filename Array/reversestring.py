def rev_rd(s):
	word=[]
	length=len(s)

	space=[' ']
	i=0
	while i<length:
		if s[i] not in space:
			word_start =i
			while i < length and s[i] not in space:
				i+=1
				words.append(s[word_start:i])
			i +=1


	return " ".join(reversed(word))

def rev_word(s):
	word=[]
	i=0
	while i <len(s)-1:
		k=0
		ad=''
		while k ==0:
			if s[i]==" ":
				i+=1
				k=1
			else:
				ad +=s[i]
				i+=1
		if len(ad)>0:
			word.append(ad)

	return ' '.join(reversed(word))		





def revs(s):
	return ' '.join(s.split()[::-1]) 

print(rev_word(' hello Jhon '))