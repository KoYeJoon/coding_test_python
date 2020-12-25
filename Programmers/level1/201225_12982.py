def solution(d, budget):
    d.sort()
    temp = []
    for i in d:
        if sum(temp)+i > budget :
            break
        else :
            temp.append(i)
    return len(temp)
# def solution(d, budget):
#     d.sort()
#     while budget < sum(d) :
#         d.pop()
#     return len(d)

print(solution([1,3,2,5,4],9))