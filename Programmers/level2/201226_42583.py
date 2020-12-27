def solution(bridge_length, weight, truck_weights):
    answer = 1
    ing_truck = []
    temp = []
    while True:
        if len(temp)>0 and temp[0] == bridge_length :
            ing_truck.pop(0)
            temp.pop(0)
        if sum(ing_truck)+truck_weights[0] <= weight :
            temp.append(0)
            ing_truck.append(truck_weights.pop(0))
        if len(truck_weights)==0 :
            answer+=(bridge_length)
            break
        for i in range(len(temp)) :
            temp[i] += 1
        answer += 1
    return answer

print(solution(100,100,[10]))