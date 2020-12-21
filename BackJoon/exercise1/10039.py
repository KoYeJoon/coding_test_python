#10039.py
sum = 0
for i in range(5) :
	a = int(input())
	if(a>40) :
		sum = sum+a
	else:
		sum = sum+40

print(sum//5)
