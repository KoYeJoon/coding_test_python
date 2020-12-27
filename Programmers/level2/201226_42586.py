def solution(progresses, speeds):
    answer = [1]
    complete_days=[]
    for i in range(len(progresses)):
        if (100-progresses[i])%speeds[i] == 0:
            complete_days.append((100-progresses[i])//speeds[i])
        else :
            complete_days.append((100-progresses[i])//speeds[i]+1)

    temp = complete_days[0]
    for i in range(1,len(complete_days)) :
        if complete_days[i] > temp :
            temp=complete_days[i]
            answer.append(1)
        elif complete_days[i] <= temp:
            answer[-1] = answer[-1]+1

    return answer

print(solution([93, 30, 55],[1, 30, 5]))