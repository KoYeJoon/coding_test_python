def solution(name):
    temp=[]
    right_left = 0
    for i in name:
        if ord(i)-ord('A') < ord('Z')-ord(i)+1 :
            temp.append(ord(i)-ord('A'))
        else :
            temp.append(ord('Z')-ord(i)+1)

    tmp = list(temp)
    pos=0
    while True :
        tmp[pos]=0
        if sum(tmp)==0 :
            break
        else :
            temp_pos = 0
            num = len(temp)+1
            for j in range(len(tmp)) :
                if tmp[j] != 0 :
                    if num > min(abs(j-pos),abs(abs(len(temp)+pos)-j)):
                        temp_pos = j
                        num = min(abs(j-pos),abs(abs(len(temp)+pos)-j))
            right_left += num
            pos = temp_pos
    #print(temp,right_left)
    return sum(temp)+right_left

print(solution("ABAAAAAAAAABB"))