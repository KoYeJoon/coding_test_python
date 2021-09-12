def check(idx,col):
    global answer
    n=len(col)
    if promising(idx,col) :
        if idx==n-1:
            answer += 1
        else :
            for j in range(n):
                col[idx+1] = j
                check(idx+1,col)


def promising(idx,col):
    for k in range(idx):
        if (col[idx]==col[k]) or (abs(col[idx]-col[k])==idx-k) :
            return False
    return True

def solution(n):
    global answer
    answer = 0

    for i in range(n):
        col = [i] + [0]*(n-1)
        check(0,col)
    return answer

print(solution(4))