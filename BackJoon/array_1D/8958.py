#8958.py
N = int(input())

for i in range(N) :
	str = input()
	score = 0
	count = 0
	for j in range(len(str)):
		if str[j] == 'O' :
			count = count+1
			score = score+count
		else:
			count=0
	print(score)
