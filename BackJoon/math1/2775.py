T = int(input())
for i in range(T) :
	k = int(input())
	n = int(input())
	bunja = 1
	bunmo = 1
	for i in range(1,n):
		bunja = bunja*(n+k-(i-1))
		bunmo = bunmo*i
	print(bunja//bunmo)
		
