'''
8 5
1 5 4 3 2 4 5 2
'''
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
temp = list(map(int,input().split()))

weight = [0]*(m+1)

for i in temp :
    weight[i] += 1

result = 0
for i in range(1,m):
    if weight[i] > 0 :
        result += (weight[i]*sum(weight[i+1:]))

print(result)