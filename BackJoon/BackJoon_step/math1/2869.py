a,b,v = map(int, input().split())
count =0
count = (v-b)//(a-b)
if (v-b)%(a-b) == 0 :
	print(count)
else :
	print(count+1)
