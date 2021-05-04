import sys
input = sys.stdin.readline

s = list(input().rstrip())
s_n = list(map(int,s))

result = s_n[0]
for i in s_n[1:] :
    if i <=1 or result <= 1:
        result += i
    else :
        result *= i

print(result)