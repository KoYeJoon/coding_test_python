#1110.py
n = int(input())
count =0
temp = 100
while(True) :
	if count==0 :
		temp = n
	count = count+1
	a = temp//10
	b = temp%10
	num = a+b
	temp = b*10 + (num%10)
	if(temp == n):
		break

print(count)
