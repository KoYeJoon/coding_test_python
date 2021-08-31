# def solution(n):
#     answer = []
#     def hanoi(n,start,end,aux):
#         if n==1 :
#             return [start,end]
#         answer.append(hanoi(n-1,start,aux,end))
#         answer.append([start,end])
#         answer.append(hanoi(n-1,aux,end,start))
#
#     hanoi(n,1,3,2)
#     answer = list(filter(None,answer))
#     return answer

def hanoi(n,start,end,aux):
    if n==1 :
        return [[start,end]]
    return hanoi(n-1,start,aux,end)+[[start,end]]+hanoi(n-1,aux,end,start)

def solution(n):
    answer = hanoi(n,1,3,2)
    return answer



print(solution(3))