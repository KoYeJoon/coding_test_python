'''
5
2 3 1 2 2
'''
import sys

input = sys.stdin.readline
n = int(input())
danger = list(map(int,input().split()))

danger.sort()

group = 0
person = 0
for i in danger :
    person += 1
    if i <= person :
        group += 1
        person = 0

print(group)