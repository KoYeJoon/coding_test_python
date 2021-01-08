def solution(s):
    answer = ''
    temp = 0
    for i in s :
        if i == ' ':
            answer += ' '
            temp = 0
        elif temp == 0:
            answer += i.upper()
            temp += 1
        else :
            answer += i.lower()

    return answer

print(solution("3people unFollowed me"))