#1065.py
def hansu(n):
	count = 0
	for i in range(1,n+1):
		if i<=99:
			count = count+1
		else:
			nums=list(map(int,str(i)))
			if nums[0]-nums[1] == nums[1]-nums[2]:
				count = count+1

	return count

a = int(input())
print(hansu(a))
