# def solution(enter, leave):
#     answer = []
#     enter_time = {}
#     leave_time ={}
#     n=len(enter)
#
#     for i in range(n):
#         enter_time[enter[i]] = i
#         leave_time[leave[i]] = i
#
#
#     meeting_person = [set() for _ in range(n+1)]
#     for i in range(1,n+1):
#         i_enter = enter_time[i]
#         i_leave = leave_time[i]
#         for j in range(1,n+1) :
#             if i != j and j not in meeting_person[i]:
#                 if enter_time[j] < i_enter and leave_time[j] > i_leave :
#                     for k in range(enter_time[j]+1,i_enter + 1):
#                         meeting_person[enter[k]].add(j)
#                         meeting_person[j].add(enter[k])
#                 elif enter_time[j] > i_enter and leave_time[j] < i_leave :
#                     for k in range(i_enter+1,enter_time[j]+1):
#                         meeting_person[i].add(enter[k])
#                         meeting_person[enter[k]].add(i)
#
#
#     for i in range(1,n+1):
#         answer.append(len(meeting_person[i]))
#
#     return answer

def solution(enter,leave):
    answer = [0] * len(enter)

    room = []
    enter_idx = 0
    # 떠나는 멤버 기준으로 시작 !
    for l in leave:
        # 현재 떠나는 멤버가 도착할 때까지 room에 인원수를 추가해준다.
        while l not in room :
            room.append(enter[enter_idx])
            enter_idx+=1
        # 현재 떠나는 멤버를 떠나보낸다.
        room.remove(l)
        # 떠나는 멤버는 현재 룸에 존재하여 만나는 인원수를 기록한다.
        answer[l-1] += len(room)

        # room에 있는 인원들은 현재 떠나는 멤버와 있었다는 의미로 1 더해준다.
        for person in room :
            answer[person-1] += 1

    return answer
print(solution([3, 2, 1], [1, 3, 2]))