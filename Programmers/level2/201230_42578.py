# def solution(clothes):
#     answer =1
#     clothes_dic = dict()
#     for i in range(len(clothes)):
#         if clothes[i][1] in clothes_dic :
#             clothes_dic[clothes[i][1]].append(clothes[i][0])
#         else:
#             clothes_dic[clothes[i][1]] = [clothes[i][0]]
#
#     for j in clothes_dic.keys():
#         answer *= (len(clothes_dic[j])+1)
#     answer -= 1
#     return answer


def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    print(cnt,[kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"],
                ['green_turban', 'headgear']]))

dict2 = {}
print(type(dict2))