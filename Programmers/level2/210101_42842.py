import math
def solution(brown, yellow):
    answer = []
    square = brown - 4
    square /= 2
    yellow_yaksu = []
    for i in range(1,int(math.sqrt(yellow))+1):
        if yellow%i == 0:
            yellow_yaksu.append((i,yellow // i))

    for i in yellow_yaksu :
        if i[0] + i[1] == square :
            answer.append(i[1]+2)
            answer.append(i[0]+2)
            break
    return answer

print(solution(10,2))
