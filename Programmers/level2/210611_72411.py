from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for cnt in course:
        temp = []
        for order in orders:
            if len(order) >= cnt :
                order = ''.join(sorted(list(order)))
                combi = list(combinations(order,cnt))
                temp += combi

        c = Counter(temp)
        temp_cnt = c.most_common()
        if len(temp_cnt)>0 and temp_cnt[0][1]>1:
            max_cnt = temp_cnt[0][1]
            answer.append(''.join(temp_cnt[0][0]))

        for i in range(1,len(temp_cnt)):
            if temp_cnt[i][1] == max_cnt:
                answer.append(''.join(temp_cnt[i][0]))
            else :
                break

        answer.sort()

    return answer

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))