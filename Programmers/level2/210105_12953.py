def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, (a % b))

def solution(arr):
    answer = 1
    for i in arr:
        answer = (answer * i) / gcd(answer, i)
    return answer

print(solution([1,2,3]))