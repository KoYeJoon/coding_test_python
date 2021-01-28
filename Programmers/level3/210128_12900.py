def solution(n):
    answer = 1
    fib0 = 1
    fib1 = 1
    if n == 1 :
        return 1
    if n==2 :
        return 2
    for i in range(n-1):
        answer = fib1 + fib0
        answer = answer % 1000000007
        fib0 = fib1 % 1000000007
        fib1 = answer % 1000000007
    return answer

print(solution(4))