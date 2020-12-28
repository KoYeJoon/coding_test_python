def solution(numbers):
    list_num = list(map(str,numbers))
    list_tuple = []
    answer =''
    if sum(numbers)==0 :
        return '0'
    for i in range(len(numbers)) :
        tmp = ''
        len_n = len(list_num[i])
        for j in range(6):
            if len_n <= j :
                list_tuple[i] += tuple(tmp[j%len_n])
            else :
                if j== 0:
                    tmp = list_num[i]
                    list_tuple.append(tuple(str(len_n)))
                    list_tuple[i] += tuple(list_num[i][j])
                else :
                    list_tuple[i] += tuple(list_num[i][j])

    list_tuple.sort(key=lambda x: (x[1],x[2],x[3],x[4],x[5]),reverse=True)
    for i in range(len(list_tuple)) :
        for j in range(1,int(list_tuple[i][0])+1) :
            answer += list_tuple[i][j]
    return answer



# def solution(numbers):
#     numbers = list(map(str, numbers))
#     numbers.sort(key=lambda x: x*3, reverse=True)
#     return str(int(''.join(numbers)))





print(solution([221,2,10]))