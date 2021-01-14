def solution(record):
    answer = []
    dic_user_name = {}
    for i in range(len(record)):
        temp = record[i].split()
        if len(temp)==3 :
            dic_user_name[temp[1]] = temp[2]

    for i in range(len(record)):
        temp = record[i].split()
        if temp[0] == 'Enter' :
            answer.append(dic_user_name[temp[1]]+"님이 들어왔습니다.")
        elif temp[0] == 'Leave' :
            answer.append(dic_user_name[temp[1]]+"님이 나갔습니다.")
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))