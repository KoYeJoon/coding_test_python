#2446.py
n = int(input())
for i in range (0,n):
	print(' '*i + '*'*(2*n-1-2*i))

for i in range(1,n):
	print(' '*(n-i-1)+'*'*(2*i+1))
