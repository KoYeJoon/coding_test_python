def solution(n, lost, reserve):
    lost2=set(lost)-set(reserve)
    reserve2 = set(reserve) - set(lost)
    for i in lost2:
        if i+1 in reserve2 :
            reserve2.remove(i+1)
        elif i-1 in reserve2 :
            reserve2.remove(i-1)
        else :
            n -= 1
    return n




print(solution(5,[2,4],[1,3,5]))