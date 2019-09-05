def anagram(s1,s2):
	l1= [i.lower() for i in s1 if i !=" "]
	l2 =[i.lower() for i in s2 if i != " "]
	return sorted(l2)==sorted(l1)

def anagram_2(s1,s2):
	s1 = s1.replace(" ",'').lower()
	s2 =s2.replace(" ", '').lower()

	return sorted(s1)==sorted(s2)
def anagram_3(s1,s2):
	s1 = s1.replace(" ",'').lower()
	s2 =s2.replace(" ", '').lower()

	if len(s1)!=len(s2):
		return False

	count = {}
	for letter in s1:
		if letter in count:
			count[letter]+=1
		else:
			count[letter] =1 
	for letter in s2:
		if letter in count:
			count[letter]-=1
		else:
			count[letter]=1
	for k in count:
		if count[k]!= 0 :
			return False
	return True

	
print(anagram('clint eastwood','old west action'))
print(anagram_2('clint eastwood','old west action'))

print(anagram_3('clint eastwood','oOld west action'))

