n,m = map(int, input().split())
max_num = 0
for i in range(n) :
    data = list(map(int,input().split()))
    if max_num < min(data) :
        max_num = min(data)

print(max_num)