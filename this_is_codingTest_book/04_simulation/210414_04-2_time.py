# 시간 측정을 위해서
import time
start_time = time.time()
N = int(input())
count=0
for si in range(N+1) :
    for bun in range(60):
        for cho in range(60):
            if '3' in str(si)+str(bun)+str(cho) :
                count += 1

print(count)
end_time = time.time()
print("걸린시간 ",end_time-start_time)