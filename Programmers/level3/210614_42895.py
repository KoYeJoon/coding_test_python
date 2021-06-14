def solution(N, number):
    if N == number:
        return 1

    dp = [set() for i in range(9)]
    dp[1].add(N)

    for i in range(2,9):
        temp=int(str(N)*i)
        dp[i].add(temp)
        for cnt in range(1,i):
            for a in dp[cnt]:
                for b in dp[i-cnt]:
                    dp[i].add(a-b)
                    dp[i].add(b-a)
                    dp[i].add(a+b)
                    dp[i].add(a*b)

                if a!=0:
                    dp[i].add(b//a)
                if b!=0 :
                    dp[i].add(a//b)


        if number in dp[i]:
            return i

    return -1

print(solution(5,12))