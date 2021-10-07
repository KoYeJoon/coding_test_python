def binomial_coefficient(n,k):
    dp = [[0]*(k+1) for _ in range(n+1)]
    for r in range(n+1):
        for c in range(min(r+1,k+1)) :
            if c==0 or c==r :
                dp[r][c] = 1
            else :
                dp[r][c] = dp[r-1][c] + dp[r-1][c-1]

    return dp[n][k]

print(binomial_coefficient(5,3))