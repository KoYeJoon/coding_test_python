import heapq

def solution(jobs):
    answer = 0
    jobs_n = len(jobs)
    # 낮은 순으로 정렬된다. (최소 힙)
    heapq.heapify(jobs)
    wait_queue = []
    time,req_time,during_time=0,0,0

    while wait_queue or jobs:
        while jobs:
            if jobs[0][0]<time :
                heapq.heappush(wait_queue,heapq.heappop(jobs)[::-1])
            else :
                break


        if wait_queue:
            during_time,req_time = heapq.heappop(wait_queue)
            time += during_time
            answer += (time - req_time)
        else :
            if jobs :
                heapq.heappush(wait_queue,heapq.heappop(jobs)[::-1])
                during_time,req_time = heapq.heappop(wait_queue)
                time += (req_time-time)+during_time
                answer += (time-req_time)
            else :
                break


    answer //= jobs_n
    return answer

print(solution([[0, 3], [1, 9], [2, 6]]))