#2577.py
list=[0,0,0,0,0,0,0,0,0,0]
A=int(input())
B=int(input())
C=int(input())
n=A*B*C

while(True):
	list[(n%10)] = list[(n%10)] + 1
	n = n//10
	if(n==0):
		break

for i in list:
	print(i)

