#10817_threeNum.py
data  = list(input().split(' '))
for i in range(len(data)) :
	data[i] = int(data[i])

sorted_list = sorted(data, reverse = True)
print(sorted_list[1])
