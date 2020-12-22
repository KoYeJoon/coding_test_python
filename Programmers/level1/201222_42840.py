def solution(answers):
    answer = [0,0,0]
    temp1 = [1,2,3,4,5]
    temp2 = [2,1,2,3,2,4,2,5]
    temp3 = [3,3,1,1,2,2,4,4,5,5]
    for i in range(len(answers)) :
        if temp1[i%5]==answers[i] :
            answer[0] += 1
        if temp2[i%8]==answers[i] :
            answer[1] += 1
        if temp3[i%10]==answers[i] :
            answer[2] += 1
    result = []
    maxAns = max(answer)
    for i in range(len(answer)):
        if maxAns == answer[i] :
            result.append(i+1)
    return result

print(solution([1,2,3,4,5]))