def solution(n):
    answer = ''
    world_124=['1','2','4']
    while True :
        n=n-1
        answer += world_124[n%3]
        n //= 3
        if n<2 :
            if n%3 != 0:
                answer+=world_124[n%3-1]
            return answer[::-1]



print(solution(10))