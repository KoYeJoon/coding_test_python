# TIL정리
def solution(N, stages):
    stages.sort()
    count_stage = []
    answer=[]

    for i in range(1,N+2):
        count_stage.append(stages.count(i))

    stage_failure={}
    for i in range(N) :
        index=0
        if i+1 in stages:
            index = stages.index(i+1)
        stage_failure[i+1] = count_stage[i]/len(stages[index:])


    temp = sorted(stage_failure.items(), key=lambda x : x[1], reverse=True)
    for i in range(N):
        answer.append(temp[i][0])

    return answer

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))