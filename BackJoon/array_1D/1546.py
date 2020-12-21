#1546.py
n = int(input())
sum=0
data = list(map(int,input().split()))

m = max(data)

for i in range(0,n):
	data[i] = data[i] / m * 100

for i in data:
	sum = sum+i

print(sum/n)
