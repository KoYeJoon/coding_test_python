def solution(n, s):
    answer = []
    if s//n == 0 :
        return [-1]

    for i in range(n):
        ans = s//(n-i)
        answer.append(ans)
        s -= ans

    answer.sort()
    return answer

print(solution(2,9))