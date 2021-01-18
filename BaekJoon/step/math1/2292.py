#2292.py
N = int(input())
room = 1
rule = 1
num = 1
if(N==1) :
	print(1)
else :
	while True :
		num+= 6*rule
		room += 1
		if(N<=num):
			break
		rule += 1
	print(room)
