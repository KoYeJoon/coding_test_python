def solution(arr1, arr2):
    answer = [[0 for j in range(len(arr2[0]))] for i in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            for k in range(len(arr2[0])):
                answer[i][k] += arr1[i][j]*arr2[j][k]
    return answer


print(solution(
    [[1, 2, 3], [4, 5, 6]],
    [[1, 4], [2, 5], [3, 6]]
))