def solution(s):
    answer = 0
    list_s = [s[0]]
    i=1
    while i<len(s):
        if len(list_s)>0 and list_s[-1]==s[i] :
            list_s.pop()
        else :
            list_s.append(s[i])
        i+=1
    if len(list_s)==0:
        answer = 1
    return answer

print(solution("baabaa"))