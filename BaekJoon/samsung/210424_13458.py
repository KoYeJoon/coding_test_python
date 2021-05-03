import sys
input = sys.stdin.readline

n = int(input())
class_n = list(map(int,input().split()))
b,c = map(int,input().split())

count = 0

for i in range(n):
    count += 1
    class_n[i] -= b
    if class_n[i]>0 :
        count += (class_n[i] // c)
        if class_n[i] % c != 0:
            count += 1

print(count)