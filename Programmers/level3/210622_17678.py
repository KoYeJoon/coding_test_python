import heapq

def solution(n, t, m, timetable):
    answer = ''
    # 분 단위로 바꿔서 생각
    minute = 9*60
    total = len(timetable)
    timetables_minute = []
    timetables_minute2 = []
    for time in timetable :
        temp_hour,temp_minute = map(int,time.split(':'))
        heapq.heappush(timetables_minute,temp_hour*60+temp_minute)

    people = [m]*n
    last_time = heapq.heappop(timetables_minute)
    for i in range(n):
        while len(timetables_minute2)< total :
            if last_time <= minute :
                if people[i] > 0 :
                    people[i] -= 1
                    timetables_minute2.append(last_time)
                    if timetables_minute :
                        last_time = heapq.heappop(timetables_minute)
                    else :
                        break
                else :
                    break
            else :
                break

        minute += t

    minute -= t
    if people[-1]>0 :
        temp_hour = minute // 60
        temp_minute = minute % 60
        answer += '%02d:%02d'%(temp_hour,temp_minute)

    else :
        temp_hour = (timetables_minute2[-1]-1) // 60
        temp_minute =  (timetables_minute2[-1]-1) % 60
        answer += '%02d:%02d'%(temp_hour,temp_minute)


    return answer

print(solution(1,1,5,["08:00", "08:01", "08:02", "08:03"]))