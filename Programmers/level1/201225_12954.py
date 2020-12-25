# def solution(x, n):
#       x가 0일때 런타임에러..!
#     return list(range(x,x*n+1,x))

def solution(x,n):
    return [x*i for i in range(1, n+1)]

print(solution(2,5))