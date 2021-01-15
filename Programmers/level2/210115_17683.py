def solution(m, musicinfos):
    answer = ''
    music_time_dic = {}
    music_come_dic = {}
    music_total_dic = {}
    for i in range(len(musicinfos)):
        temp = musicinfos[i].split(',')
        time1 = temp[0].split(':')
        time2 = temp[1].split(':')
        total = (int(time2[0])*60 + int(time2[1])) - (int(time1[0])*60 + int(time1[1]))
        j=0
        count = 0
        while count<total :
            if j<len(temp[3])-1 :
                if temp[3][j+1] == '#':
                    if temp[2] in music_time_dic :
                        music_time_dic[temp[2]].append(temp[3][j] + '#')
                    else :
                        music_time_dic[temp[2]] = [temp[3][j] + '#']
                    j+=1
                else :
                    if temp[2] in music_time_dic :
                        music_time_dic[temp[2]].append(temp[3][j])
                    else :
                        music_time_dic[temp[2]] = [temp[3][j]]

            else :
                if temp[2] in music_time_dic :
                    music_time_dic[temp[2]].append(temp[3][j])
                else :
                    music_time_dic[temp[2]] = [temp[3][j]]

            count += 1
            j += 1
            if j == len(temp[3]) :
                j=0
        music_come_dic[temp[2]] = len(musicinfos)-i
        music_total_dic[temp[2]] = total

    m_len = len(m) - m.count('#')
    flag=0
    music_time_dic = sorted(music_time_dic.items(),key = lambda x : (music_total_dic[x[0]],music_come_dic[x[0]]),reverse=True)
    for i in music_time_dic:
        for j in range(len(i[1])) :
            if m == ''.join(i[1][j:j+ m_len]):
                flag=1
                break
        if flag ==1 :
            answer = i[0]
            break
    else :
        answer = '(None)'

    return answer
print(solution("CC#BCC#BCC#BCC#B", ["13:40,14:10,FOO,CC#B", "03:50,04:20,BAR,CC#B"]))