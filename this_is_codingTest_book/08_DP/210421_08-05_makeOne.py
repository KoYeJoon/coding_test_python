x = int(input())

# dp 테이블 초기화
dp = [0] * 10001

# 다이나믹 프로그래밍 진행 (보텀업 )
for i in range(2, x+1):
    # 현재의 수에서 1을 빼는 경우
    dp[i] = dp[i-1]+1
    # 현재의 수가 2로 나누어 떨어지는 경우
    # 현재의 수와 // 현재의 수를 2로 나누었을 때의 경우의 수에서 2로 나누는 경우의 수를 더했을 때(+1) 중 작은 수를 dp 테이블에 저장한다 .
    if i%2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i%3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
    if i%5 == 0:
        dp[i] = min(dp[i], dp[i//5]+1)

print(dp[x])