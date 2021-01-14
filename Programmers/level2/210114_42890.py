# import itertools
# def solution(relation):
#     answer = 0
#     row = len(relation)
#     col = len(relation[0])
#     col_mark = [0 for i in range(col)]
#     count = 1
#     while count<=col :
#         temp_mark_idx=[]
#         for a in range(len(col_mark)):
#             if col_mark[a] == 0:
#                 temp_mark_idx.append(a)
#
#         if len(temp_mark_idx) < count:
#             break
#
#         combi_list = list(itertools.combinations(temp_mark_idx,count))
#
#         for a in range(len(combi_list)) :
#             rel_temp = []
#             for b in range(row) :
#                 temp = []
#                 for c in combi_list[a]:
#                     temp.append(relation[b][c])
#                 rel_temp.append(temp)
#
#
#             for b in range(row) :
#                 if rel_temp.pop() in rel_temp :
#                     break
#             else :
#                 answer += 1
#                 for b in combi_list[a] :
#                     col_mark[b] = 1
#
#         count += 1
#
#     return answer

'''
위에 코드는 1,2 column이 후보키이고 1,3,4 또한 후보키인 경우와 같을 때 작동이 안됨.
너무 단순하게 생각한 경우이다!
'''
import itertools
def solution(relation):
    row = len(relation)
    col = len(relation[0])
    count = 1
    key_set = set()
    while count<=col :
        temp_mark_idx=[i for i in range(col)]
        combi_list = list(itertools.combinations(temp_mark_idx,count))
        for a in range(len(combi_list)) :
            rel_temp = []
            for b in range(row) :
                temp = []
                for c in combi_list[a]:
                    temp.append(relation[b][c])
                rel_temp.append(temp)

            for b in range(row) :
                if rel_temp.pop() in rel_temp :
                    break
            else :
                for c in key_set :
                    if set(c).issubset(set(combi_list[a])) :
                        break
                else :
                    key_set.add(combi_list[a])

        count += 1

    return len(key_set)

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))