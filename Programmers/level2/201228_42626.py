# def solution(scoville, K):
#     answer = 0
#     while scoville[0]<=K :
#         if len(scoville)==1 :
#             return -1
#         answer+=1
#         scoville.append(scoville.pop(0)+scoville.pop(0)*2)
#         scoville.sort()
#     return answer

#heap 사용 정리
import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0]<=K :
        if len(scoville)==1 :
            return -1
        answer+=1
        heapq.heappush(scoville,heapq.heappop(scoville) + heapq.heappop(scoville)*2)
    return answer

print(solution([1, 2, 3, 9, 10, 12],7))

