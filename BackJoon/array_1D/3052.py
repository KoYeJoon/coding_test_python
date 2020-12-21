#3052.py
list = []
for i in range(10):
	a = int(input())
	list.append(a%42)

list = set(list)
print(len(list))
