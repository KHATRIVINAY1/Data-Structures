import timeit
def fibo(n):

	if n==0 or n==1:
		return n
	else:
		return fibo(n-1)+fibo(n-2)

def fibo_ite(n):
	a=0
	b=1
	for i in range(n):
		a,b = b, a+b
	
	return a



print(fibo_ite(10))
print(fibo(10))