def solution(s):
    answer = len(s)
    for i in range(1,len(s)//2+1):
        compressed_n = 0
        temp = s[:i]
        cnt = 1
        for j in range(i,len(s),i):
            if temp == s[j:j+i] :
                cnt += 1
            else :
                temp_n =  len(str(cnt)) + i if cnt>1 else i
                compressed_n += temp_n
                temp = s[j:j+i]
                print(i,j,j+i,temp)
                cnt = 1

        if cnt > 1:
            compressed_n += len(str(cnt)) + i
        else :
            compressed_n += len(temp)
        answer = min(answer,compressed_n)

    return answer

print(solution("abcabcdede"))
