def solution(play_time, adv_time, logs):
    if play_time == adv_time :
        return '00:00:00'

    answer = ''
    # convert hour ,minute to second
    play_time_list = play_time.split(':')
    play_time_second = int(play_time_list[0])*60*60 + int(play_time_list[1])*60 + int(play_time_list[2])

    adv_time_list = adv_time.split(':')
    adv_time_second = int(adv_time_list[0])*60*60 + int(adv_time_list[1])*60 + int(adv_time_list[2])

    # time, people 변화
    time_stamp= []
    for i in logs :
        temp = i.split('-')
        start_time_list = temp[0].split(':')
        end_time_list = temp[1].split(':')

        start_time_second = int(start_time_list[0])*60*60 + int(start_time_list[1])*60 + int(start_time_list[2])
        end_time_second = int(end_time_list[0])*60*60 + int(end_time_list[1])*60 + int(end_time_list[2])

        time_stamp.append([start_time_second,1])
        time_stamp.append([end_time_second,-1])

    time_stamp.sort()

    n = 1
    accum_dict = {}
    temp_start = time_stamp[0][0]
    for i in range(1,len(time_stamp)):
        accum_dict[temp_start] = n * (time_stamp[i][0]-temp_start)
        print(temp_start,n * (time_stamp[i][0]-temp_start))
        temp_start = time_stamp[i][0]
        n += time_stamp[i][1]




    accum_dict_items = sorted(list(accum_dict.items()))

    s = 0
    answer_time = 0
    max_accum_time = 0
    while s < len(accum_dict_items):
        temp_time = 0
        end_time = accum_dict_items[s][0] + adv_time_second
        for i in range(s+1,len(accum_dict_items)):
            if end_time > accum_dict_items[i][0] :
                temp_time += accum_dict_items[i-1][1]
            else :
                if accum_dict_items[i][0] == end_time :
                    temp_time += accum_dict_items[i][1]
                else :
                    temp_time += accum_dict_items[i][1] // (accum_dict_items[i][0]-end_time)
                break
        if max_accum_time < temp_time :
            max_accum_time = temp_time
            answer_time = accum_dict_items[s][0]

        s += 1

    answer = str(answer_time//3600).zfill(2) + ":"
    answer_time -= (answer_time//3600) * 3600
    answer += str(answer_time//60).zfill(2) + ":"
    answer_time -= (answer_time//60) * 60
    answer += str(answer_time%60).zfill(2)
    return answer

print(solution("02:03:55","00:14:15",["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))