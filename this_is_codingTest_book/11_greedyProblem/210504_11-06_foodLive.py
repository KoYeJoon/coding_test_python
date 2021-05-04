import heapq
def solution(food_times, k):
    if sum(food_times) <= k :
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q,(food_times[i],i+1))

    count = 0
    temp = 0
    while k > 0:
        count = q[0][0] - temp
        if k < len(q)*count :
            break
        k -= len(q)*count
        i = 1
        temp = heapq.heappop(q)[0]
        while i<len(q):
            if q[i][0] > temp:
                break
            heapq.heappop(q)

    result = sorted(q,key=lambda x : x[1])
    return result[k%len(q)][1]

print(solution(food_times=[4,2,3,6,7,1,5,8], k=27))