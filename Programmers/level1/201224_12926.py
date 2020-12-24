def solution(s, n):
    # 다른 사람의 풀이를 보니 아스킼 값을 통해 하는 방법도 있었다 !
    answer=''
    alpha_big= ['A','B','C','D','E','F','G','H','I','J','K',
            'L','M','N','O','P','Q','R','S','T','U','V',
            'W','X','Y','Z']
    alpha_small = ['a','b','c','d','e','f','g','h','i','j','k',
                   'l','m','n','o','p','q','r','s','t','u','v',
                   'w','x','y','z']
    for i in s:
        if i==' ':
            answer += ' '
        elif i in alpha_small :
            answer+=alpha_small[alpha_small.index(i)+n if alpha_small.index(i)+n<26 else alpha_small.index(i)+n-26]
        else :
            answer+=alpha_big[alpha_big.index(i)+n if alpha_big.index(i)+n<26 else alpha_big.index(i)+n-26]


    return answer

print(solution("a B z",4))