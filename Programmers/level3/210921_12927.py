# def solution(n, works):
#     answer = 0
#     for _ in range(n):
#         max_n =max(works)
#         if max_n==0 :
#             break
#         i = works.index(max_n)
#         works[i] -= 1
#
#     for work in works :
#         answer += work*work
#
#     return answer

def solution(n, works):
    answer = 0
    work_dict = {}
    for work in works :
        if work not in work_dict :
            work_dict[work] = 1
        else :
            work_dict[work] += 1

    while n > 0 :
        keys = work_dict.keys()
        max_n = max(keys)
        if n>=work_dict[max_n] :
            n -= work_dict[max_n]
            if max_n-1<0 :
                break
            if max_n-1 not in work_dict :
                work_dict[max_n-1] = work_dict[max_n]
            else :
                work_dict[max_n-1]+=work_dict[max_n]
            del work_dict[max_n]
        else :
            work_dict[max_n] -= n
            if max_n-1<0 :
                break
            if max_n-1 not in work_dict :
                work_dict[max_n-1] = n
            else :
                work_dict[max_n-1]+=n
            break

    keys = work_dict.keys()
    for key in keys :
        answer += work_dict[key] * (key*key)

    return answer


print(solution(4,[4,3,3]))