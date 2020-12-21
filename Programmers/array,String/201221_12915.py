def solution(s):
    answer=''
    temp = sorted(s,reverse=True)
    answer = ''.join(temp)
    return answer

s="Zbcdegf"
print(solution(s))