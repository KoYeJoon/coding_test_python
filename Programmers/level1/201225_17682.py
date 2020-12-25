def solution(dartResult):
    answer = []
    mark = 0
    for i in range(len(dartResult)) :
        if dartResult[i].isdigit() :
            if dartResult[i]=='1' and dartResult[i+1] == '0':
                answer.append(10)
                mark=1
            else :
                if mark == 0 :
                    answer.append(int(dartResult[i]))
                mark=0
        elif dartResult[i] in ['S','D','T'] :
            if dartResult[i] == 'D' :
                answer[-1] = answer[-1]**2
            elif dartResult[i]=='T' :
                answer[-1] = answer[-1]**3
        elif dartResult[i] in ['*','#'] :
            if dartResult[i]=='*' :
                answer[-1] = answer[-1]*2
                if len(answer)>1 :
                    answer[-2] = answer[-2]*2
            else :
                answer[-1] = -answer[-1]
    return sum(answer)

print(solution("1D2S#10S"))