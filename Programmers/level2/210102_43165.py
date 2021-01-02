# def solution(numbers, target):
#     answer = 0
#     temp = [numbers[0],-numbers[0]]
#     k=0
#     for i in range(1,len(numbers)):
#         for j in range(k,k+pow(2,i)):
#             temp.append(temp[j]+numbers[i])
#             temp.append(temp[j]-numbers[i])
#         k += pow(2,i)
#
#     for i in range(k,k+pow(2,len(numbers))):
#         if temp[i] == target :
#             answer += 1
#     return answer


from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    print(l,s)
    return s.count(target)


# def solution(numbers, target):
#     if not numbers and target == 0 :
#         return 1
#     elif not numbers:
#         return 0
#     else:
#         return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])

# answer = 0
# def DFS(idx, numbers, target, value):
#     global answer
#     N = len(numbers)
#     if(idx== N and target == value):
#         answer += 1
#         return
#     if(idx == N):
#         return
#
#     DFS(idx+1,numbers,target,value+numbers[idx])
#     DFS(idx+1,numbers,target,value-numbers[idx])
# def solution(numbers, target):
#     global answer
#     DFS(0,numbers,target,0)
#     return answer

print(solution([1, 1, 1],2))