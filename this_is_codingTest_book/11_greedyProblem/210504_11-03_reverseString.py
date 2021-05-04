import sys
input = sys.stdin.readline

s = input().rstrip()
result = 1

for i in range(1,len(s)):
    if s[i-1] != s[i] :
        result += 1

print(result//2)