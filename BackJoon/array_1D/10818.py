#10818.py
n = int(input())
min = 1000001
max = -1000001

a = list(map(int,input().split()))

for i in a:
	if(min>i):
		min=i
	if(max<i):
		max=i

print(min, max)
