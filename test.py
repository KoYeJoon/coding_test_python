n=int(input())

fib0 = 1
fib1 = 1
fib = 0
for i in range(n-1):
	fib = fib0+fib1
	fib0 = fib1
	fib1 = fib

if n == 1:
	print(1)
else :
	print(fib)	
