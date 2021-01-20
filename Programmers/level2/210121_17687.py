def jinsu_rec(a,b):
    convertString="0123456789ABCDEF"
    if a <b :
        return convertString[a]
    n = divmod(a,b)
    return jinsu_rec(a//b, b)+ convertString[n[1]]


def solution(n, t, m, p):
    answer = ''
    count = 0
    total_jinsu = []
    while len(total_jinsu) < m*t :
        temp = list(jinsu_rec(count,n))
        total_jinsu += temp
        count += 1

    for i in range(m*t):
        if i%m == p-1 :
            answer += total_jinsu[i]
    return answer

print(solution(2,4,2,1))