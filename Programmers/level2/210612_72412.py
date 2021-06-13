from itertools import combinations
# def solution(info, query):
#     answer = []
#     table = []
#     temp_table = [['cpp','java','python'],['backend','frontend'],
#                   ['junior','senior'],['chicken','pizza']]
#     for i in info:
#         list_i = list(i.split())
#         list_i[4]=int(list_i[4])
#         table.append(list_i)
#
#     table.sort(key =lambda x : x[4])
#
#     for q in query :
#         q_split = q.split('and')
#         count = 0
#         temp = q_split[3]
#         temp = list(temp.split())
#         q_split[3] = temp[0]
#         score = int(temp[1])
#         for i in range(len(q_split)):
#             q_split[i] = q_split[i].strip()
#             if q_split[i]=='-':
#                 q_split[i]=temp_table[i]
#
#         for lan,dep,rec,food,sco in table :
#             if (sco >= score) and (lan in q_split[0]) and (dep in q_split[1] )and (rec in q_split[2]) and (food in q_split[3]) :
#                 count += 1
#
#         answer.append(count)
#     return answer

def solution(info, query):
    answer = []
    table = {}

    for i in info :
        i_split = i.split()
        table_keys=[]
        for k in range(5):
            for li in combinations([0, 1, 2, 3], k):
                case = ''
                for idx in range(4):
                    if idx not in li :
                        case += i_split[idx]
                    else :
                        case += '-'
                table_keys.append(case)
        for table_key in table_keys:
            if table_key not in table.keys() :
                table[table_key] = [int(i_split[4])]
            else :
                table[table_key].append(int(i_split[4]))

    for key in table.keys():
        table[key].sort()

    for q in query :
        q_split = q.split()
        real_q = q_split[0]+ q_split[2] + q_split[4] + q_split[6]
        score = int(q_split[7])
        if real_q in table.keys():
            start,end = 0,len(table[real_q])
            while start <= end and start != len(table[real_q]):
                mid = (start+end)//2
                if table[real_q][mid] >= score:
                    end = mid -1
                else :
                    start = mid+1
            answer.append(len(table[real_q])-start)
        else :
            answer.append(0)
    return answer


print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
               ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))