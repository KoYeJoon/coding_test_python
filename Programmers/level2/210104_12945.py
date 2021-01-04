# 시간 초과된 재귀법
# def solution(n):
#     answer = 0
#     if n==0 :
#         return 0
#     if n==1 :
#         return 1
#
#     return solution(n-1)+solution(n-2)

def solution(n):
    answer = 0
    if n==0 :
        return 0
    if n==1 :
        return 1
    fib1 = 0
    fib2 = 1
    for i in range(n):
        answer = fib1 + fib2
        fib2 = fib1
        fib1 = answer
    return answer%1234567

print(solution(3))