#10996.py
a = int(input())
b,c = a, a//2
for i in range(1,a+1):
	if b%2 ==1:
		print('* '*(b-c))
		print(' *'*c)
	elif b%2 == 0:
		print('* '*c)
		print(' *'*(b-c))
