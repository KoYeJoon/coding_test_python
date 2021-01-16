#4344.py
for i in range(int(input())):
	list_arr = list(map(int, input().split(' ')))
	ave = sum(list_arr[1:])/list_arr[0]
	count=0
	for j in list_arr[1:]:
		if j>ave:
			count=count+1
	print(str('%.3f'%round(count/list_arr[0]*100,3))+"%")
