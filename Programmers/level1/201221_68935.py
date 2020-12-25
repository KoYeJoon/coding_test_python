def solution(n):
    answer = 0
    three_base=[]

    while n != 0 :
        three_base.append(n%3)
        n=n//3

    answer = ''.join(three_base)
    answer = int(answer,3)
    # for i in range(len(three_base)) :
    #     answer = answer + three_base[i]*pow(3,len(three_base)-i-1)

    return answer


print(solution(45))