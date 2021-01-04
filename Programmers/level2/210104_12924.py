# def solution(n):
#     answer = 1
#     if n<3 :
#         return 1
#     for i in range(1,n//2+1):
#         sum=0
#         for j in range(n//2-i+2):
#             sum += i+j
#             if sum==n :
#                 answer+=1
#                 break
#             elif sum>n :
#                 break
#     return answer

def solution(num):
    return len([i  for i in range(1,num+1,2) if num % i is 0])

print(solution(15))