def solution(arr1, arr2):
    answer =[[]]
    for i in range(len(arr1)) :
        temp=[]
        for j in range(len(arr1[i])) :
            temp.append(arr1[i][j]+arr2[i][j])
        answer.append(temp)
    answer = answer[1:]
    return answer

print(solution([[1,2],[2,3]],[[3,4],[5,6]]))