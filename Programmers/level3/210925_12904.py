def solution(s):
    answer = len(s)
    len_s = len(s)
    while answer > 0:
        for i in range(len_s-answer+1):
            temp_s = s[i:i+answer]
            for j in range(answer//2):
                if temp_s[j] != temp_s[answer-j-1] :
                    break
            else :
                return answer
        answer -= 1

    return answer


print(solution("abcdcba"))