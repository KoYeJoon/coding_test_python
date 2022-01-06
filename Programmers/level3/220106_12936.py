def solution(n, k):
    answer = []
    num = [i for i in range(1,n+1)]
    tmp = 1
    fact = [1]
    for i in range(1,n+1):
        tmp *= i
        fact.append(tmp)

    while n > 1 :
        if n==2 and k==2:
            idx = 1
        elif n==2 and k==1:
            idx = 0
        elif k%fact[n-1]>0 :
            idx = k//fact[n-1]
            tmp = idx*fact[n-1]
        else :
            idx = k//fact[n-1]-1
            tmp = idx*fact[n-1]
        answer.append(num[idx])
        num.pop(idx)
        k -= tmp
        n -= 1

    answer.append(num.pop())

    return answer

print(solution(4,10))