def solution(s):
    answer = ''
    # s.split()하면 프로그래머스에서 다틀렸다고 나옴 ㅜ_ㅜ
    temp = s.split(" ")
    for i in range(len(temp)) :
        for j in range(len(temp[i])) :
            if j%2 == 0 :
                answer += temp[i][j].upper()
            else :
                answer += temp[i][j].lower()
        if i != len(temp)-1 :
            answer += ' '
    return answer

print(solution("try hello world"))