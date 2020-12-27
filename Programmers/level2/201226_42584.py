def solution(prices):
    answer=[]
    for i in range(len(prices)) :
        for j in range(i+1,len(prices)):
            if prices[i]>prices[j] :
                answer.append(j-i)
                break
            elif j==len(prices)-1 :
                answer.append(j-i)
    answer.append(0)
    return answer

# deque 설명해놓기 (코테 연습에)
# from collections import deque
# def solution(prices):
#     answer = []
#     prices = deque(prices)
#     while prices:
#         c = prices.popleft()
#
#         count = 0
#         for i in prices:
#             if c > i:
#                 count += 1
#                 break
#             count += 1
#
#         answer.append(count)
#
#     return answer
print(solution([1,2,3,2,3]))