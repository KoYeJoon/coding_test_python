def solution(s):
    answer = len(s)
    for i in range(1,len(s)):
        temp=1
        temp_s = i
        for j in range(0,len(s)-2*i+1,i):
            if s[j:j+i] == s[j+i:j+2*i]:
                temp+=1
                if j >= len(s)-3*i+1:
                    temp_s += len(str(temp))
            else :
                if temp == 1:
                    temp_s += i
                else :
                    temp_s += len(str(temp))
                    temp_s += i
                    temp = 1
        temp_s += (len(s)%i)
        if answer > temp_s :
            answer = temp_s

    return answer

print(solution("xxxxxxxxxxa"))
#print(solution("abcabcdede"))