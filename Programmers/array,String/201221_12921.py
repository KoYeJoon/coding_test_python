#에라토스테너스의 체 사용
def solution(n):
    num = set(range(2,n+1))
    for i in range(2,n+1) :
        if i in num :
            num -= set(range(2*i,n+1,i))
    return len(num)

# def solution(n):
#     if n == 2 :
#         return 1
#     elif n==3:
#         return 2
#     answer = 2
#     for i in range(5,n+1,2):
#         for j in range(3,i+1) :
#             if i%j==0:
#                 break
#             elif i-1==j :
#                 answer = answer+1
#
#     return answer

print(solution(10))