# def solution(numbers):
#     answer = []
#     for num in numbers :
#         temp = num+1
#         while True :
#             if bin(num^temp)[2:].count('1')<=2 :
#                 answer.append(temp)
#                 break
#             temp += 1
#     return answer

def solution(numbers):
    answer = []
    for num in numbers :
        if num%2 == 0 or (num//2)%2 == 0:
            answer.append(num+1)
        else :
            cnt = 0
            temp = num
            while temp >0 :
                if temp%2 == 0 :
                    answer.append(num+2**(cnt-1))
                    break
                if temp==1 :
                    answer.append(num+2**cnt)
                temp = (temp//2)
                cnt += 1
    return answer


print(solution([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))