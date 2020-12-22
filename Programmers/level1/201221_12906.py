def solution(arr):
    answer = []
    temp = arr[0]
    answer.append(temp)
    for i in range(1,len(arr)) :
        if i != len(arr) :
            if (arr[i] != temp) :
                temp = arr[i]
                answer.append(arr[i])
            else :
                i=i+2

    return answer


arr = [1,1,3,3,0,1,1]
print(solution(arr))