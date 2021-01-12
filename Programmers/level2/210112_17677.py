def solution(str1, str2):
    str1_list=[]
    str2_list = []
    intersect=0
    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha() :
            str1_list.append(str1[i:i+2].lower())
    temp = list(str1_list)
    for i in range(len(str2)-1) :
        if str2[i:i+2].isalpha() :
            str2_list.append(str2[i:i+2].lower())
            if str2[i:i+2].lower() in temp :
                intersect += 1
                temp.pop(temp.index(str2[i:i+2].lower()))


    if len(str1_list) + len(str2_list)  - intersect == 0:
        answer = 65536
    else :
        answer = int((intersect / (len(str1_list) + len(str2_list)  - intersect)) * 65536)

    return answer

print(solution("FRANCE","french"))