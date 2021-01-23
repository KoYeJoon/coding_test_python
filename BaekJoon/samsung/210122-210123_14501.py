from sys import stdin
n = int(stdin.readline())
consult = [] # 0-6
for i in range(n):
    t,p =map(int, stdin.readline().split())
    consult.append([t,p])

dp = [0 for i in range(n+1)]    # 0-7 [ 0, x]

for i in range(1,n+1):
    # i = 1
    if i+consult[i-1][0]-1 < n+1:
        # dp[3] = max (dp[3] , consult[0][1] + dp[0])
        dp[i+consult[i-1][0]-1] = max(dp[i+consult[i-1][0]-1],consult[i-1][1]+dp[i-1])
    dp[i] = max(dp[:i+1])

print(dp[-1])