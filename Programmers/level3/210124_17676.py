def solution(lines):
    # [start_time, end_time]
    time_list = []
    for i in lines :
        tmp = i.split()
        long_time = float(tmp[2][:-1])-0.001
        time = tmp[1].split(':')
        second = round(float(time[2])-long_time,3)
        minute = int(time[1])
        hour = int(time[0])
        start_time = 60*60*hour + 60*minute + second
        end_time = 60*60*hour+ 60*minute+ round(float(time[2]),3)
        time_list.append([start_time,end_time])
    max_n = 0

    for i in range(len(time_list)) :
        n1 = 0
        n2 = 0
        s1 = time_list[i][0]
        e1 = time_list[i][0]+1
        s2 = time_list[i][1]
        e2 = time_list[i][1]+1
        for j in time_list:
            if j[1] >= s1 and j[0]<e1 :
                n1 += 1
            if j[1] >= s2 and j[0]<e2 :
                n2 += 1

        if max([n1,n2]) > max_n :
            max_n = max([n1,n2])

    return max_n


print(solution(["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]))