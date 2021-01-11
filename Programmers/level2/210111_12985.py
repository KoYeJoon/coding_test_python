import math
def solution(n,a,b):
    answer = 1
    log_n = math.log2(n)
    while answer <= log_n:
        if abs(a-b)==1:
            if a//2 != b//2 :
                break
        a = (a+1) // 2
        b = (b+1) // 2
        answer+=1
    return answer

print(solution(8,4,7))