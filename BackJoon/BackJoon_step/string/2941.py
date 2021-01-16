#2941.py
a = ['c=', 'c-','dz=','d-','lj','nj','s=','z=']
alpha = input()

for t in a:
	alpha = alpha.replace(t,'a')

print(len(alpha))
