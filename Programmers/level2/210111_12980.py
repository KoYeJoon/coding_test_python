def solution(n):
    ans = 0
    while n>0 :
        if n%2 == 1:
            n -= 1
            ans += 1
        else :
            # 순간 이동하는 경우는 연료를 쓰지 않는다.
            n //= 2
    return ans

print(solution(5000))