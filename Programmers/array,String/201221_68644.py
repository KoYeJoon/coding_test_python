def solution(numbers):
    tempAnswer = []
    for i in range(0,len(numbers)) :
        for j in range(i+1,len(numbers)) :
            tempAnswer.append(numbers[i]+numbers[j])

    temp = set(tempAnswer)
    ans = list(temp)
    ans.sort()
    return ans


numbers = [2,1,3,4,1]
print(solution(numbers))