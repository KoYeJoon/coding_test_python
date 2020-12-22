# def solution(n):
#     answer = ''
#     str1 = '수'
#     str2 = '박'
#     for i in range(n) :
#         answer += str1 if i%2==0 else str2
#     return answer
def solution(n) :
    answer = "수박"*n
    return answer[:n]


print(solution(4))