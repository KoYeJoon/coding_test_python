# import math
#
# def solution(left, right):
#     answer = 0
#     # 제곱수는 약수가 홀수개, 제곱수가 아니라면 약수는 짝수개
#     for i in range(left, right+1):
#         if math.sqrt(i)-int(math.sqrt(i)) == 0:
#             answer -= i
#         else :
#             answer += i
#     return answer


def solution(left, right):
    answer = 0
    # 제곱수는 약수가 홀수개, 제곱수가 아니라면 약수는 짝수개
    for i in range(left, right+1):
        if i**0.5-int(i**0.5) == 0:
            answer -= i
        else :
            answer += i
    return answer

print(solution(13,17))