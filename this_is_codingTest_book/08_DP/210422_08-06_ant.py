n = int(input())
dp = list(map(int,input().split()))

for i in range(1,n) :
    if i== 1:
        dp[i] = max(dp[i],dp[i-1])
    else:
        dp[i] = max(dp[i-1], dp[i-2]+dp[i])

print(dp[n-1])