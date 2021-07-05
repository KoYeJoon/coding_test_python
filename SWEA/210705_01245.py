T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    temp_ball = list(map(int,input().split()))
    ball_x = temp_ball[:n]
    ball_m = temp_ball[n:]
    answer = []
    for i in range(n-1):
        left = ball_x[i]
        right = ball_x[i+1]
        for _ in range(100):
            s=0
            mid = (left + right)/2
            for k in range(i+1):
                s += ball_m[k]/((mid-ball_x[k])**2)
            for k in range(i+1,n):
                s -= ball_m[k] /((mid-ball_x[k])**2)
            if s>0 :
                left = mid
            else :
                ans = mid
                right = mid
        answer.append(ans)
    print('#%d'%test_case, end = ' ')
    for i in answer:
        print('%.10f'%i, end = ' ')

    print()