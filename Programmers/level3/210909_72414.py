def solution(play_time, adv_time, logs):
    if play_time == adv_time :
        return '00:00:00'

    # convert hour ,minute to second
    play_time_list = play_time.split(':')
    play_time_second = int(play_time_list[0])*60*60 + int(play_time_list[1])*60 + int(play_time_list[2])

    adv_time_list = adv_time.split(':')
    adv_time_second = int(adv_time_list[0])*60*60 + int(adv_time_list[1])*60 + int(adv_time_list[2])

    # time, people 변화
    dp_time_people_stamp= [0 for i in range(play_time_second+1)]
    for i in logs :
        temp = i.split('-')
        start_time_list = temp[0].split(':')
        end_time_list = temp[1].split(':')

        start_time_second = int(start_time_list[0])*60*60 + int(start_time_list[1])*60 + int(start_time_list[2])
        end_time_second = int(end_time_list[0])*60*60 + int(end_time_list[1])*60 + int(end_time_list[2])

        dp_time_people_stamp[start_time_second]+=1
        dp_time_people_stamp[end_time_second]+=-1

    for i in range(1,play_time_second+1):
        dp_time_people_stamp[i] += dp_time_peoㄴple_stamp[i-1]

    for i in range(1,play_time_second+1):
        dp_time_people_stamp[i] += dp_time_people_stamp[i-1]

    max_people = dp_time_people_stamp[adv_time_second]
    max_accum_time = 0
    for start_point in range(play_time_second-adv_time_second+1):
        if max_people < dp_time_people_stamp[start_point+adv_time_second]-dp_time_people_stamp[start_point] :
            max_people = dp_time_people_stamp[start_point+adv_time_second] - dp_time_people_stamp[start_point]
            max_accum_time = start_point+1


    hours = max_accum_time // 3600
    mins = (max_accum_time % 3600) // 60
    secs = max_accum_time % 60
    return '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)





print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:25:50-00:48:29", "00:40:31-01:00:00", "01:37:44-02:02:30", "01:30:59-01:53:29"]))