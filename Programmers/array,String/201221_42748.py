def solution(array, commands):
    answer = []
    for a in range(len(commands)) :
        i = commands[a][0]
        j = commands[a][1]
        k = commands[a][2]
        temp = array[i-1:j]
        temp.sort()
        answer.append(temp[k-1])
    return answer



array = [1,5,2,6,3,7,4]
commands = [[2,5,3],[4,4,1],[1,7,3]]

print(solution(array,commands))