# def solution(land):
#     answer = 0
#     if len(land)==1 :
#         return max(land[0])
#
#     for i in range(len(land[0])):
#         temp_arr = []
#         temp = land[1][:i] + land[1][i+1:]
#         temp_arr.append(temp)
#         for j in range(2,len(land)):
#             temp_arr.append(land[j])
#         temp_ans = land[0][i] + solution(temp_arr)
#         if answer < temp_ans :
#             answer = temp_ans
#
#     return answer

# def solution(land):
#     for i in range(1,len(land)):
#         land[i][0] = max(land[i][0]+land[i-1][1], land[i][0]+land[i-1][2], land[i][0] + land[i-1][3])
#         land[i][1] = max(land[i][1]+land[i-1][0], land[i][1]+land[i-1][2], land[i][1] + land[i-1][3])
#         land[i][2] = max(land[i][2]+land[i-1][0], land[i][2]+land[i-1][1], land[i][2] + land[i-1][3])
#         land[i][3] = max(land[i][3]+land[i-1][0], land[i][3]+land[i-1][1], land[i][3] + land[i-1][2])
#
#     return max(land[-1])

def solution(land):
    for i in range(1, len(land)):
        for j in range(len(land[0])):
            land[i][j] = max(land[i -1][: j] + land[i - 1][j + 1:]) + land[i][j]
    return max(land[-1])

print(solution([[1,2,3,5],
                 [5,6,7,100],
                 [4,3,2,1]]))

