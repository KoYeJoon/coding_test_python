import sys
input = sys.stdin.readline

s = input().rstrip()

arr = []
n = 0
for i in s :
    if i.isalpha() :
        arr.append(i)
    else:
        n += int(i)

arr.sort()
print(''.join(arr)+str(n))