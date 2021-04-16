# 시간 측정을 위해서
import time
start_time = time.time()
pos = input()
row = int(pos[1])
col = int(ord(pos[0])) - int(ord('a')) + 1

direct = [(-2,-1), (-1,-2) , (1,2), (2,1), (-1,2), (2,-1), (1,-2),(-2,1)]

result = 0
for i in direct :
    nr = row + i[0]
    nc = col + i[1]
    if nr >= 1 and nr <= 8 and nc >= 1 and nc <= 8 :
        result += 1

print(result)
end_time = time.time()
print("걸린시간 ",end_time-start_time)