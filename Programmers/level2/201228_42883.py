# def solution(number, k):
#     max_num = max(list(map(int,number)))
#     len_num = len(number)
#     for i in range(k):
#         temp = number[1:]
#         for j in range(1,len_num-i):
#             tmp2 = number[:j] + number[j+1:]
#             if temp < tmp2:
#                 temp = tmp2
#                 if temp[0] == max_num :
#                     break
#         number = temp
#     return number

# def solution(number, k):
#     tmp_arr = list(map(int,number))
#     max_num = max(tmp_arr)
#     for i in range(k):
#         max_idx = tmp_arr.index(max_num)
#         min_num=min(tmp_arr)
#         if max_idx != 0:
#             temp = tmp_arr[:max_idx]
#             tmp_arr.pop(temp.index(min(temp)))
#         elif min_num == max_num :
#             tmp_arr.pop()
#         else :
#             min_idx = tmp_arr.index(min_num)
#             tmp_arr.pop(min_idx)
#     answer = list(map(str,tmp_arr))
#     return ''.join(answer)

def solution(number, k):
    temp = [number[0]]
    for i in number[1:]:
        while len(temp)>0 and temp[-1]<i and k>0 :
            k -= 1
            temp.pop()
        temp.append(i)

    if k!= 0:
        temp = temp[:-k]
    return  ''.join(temp)





print(solution(	"90292", 2))