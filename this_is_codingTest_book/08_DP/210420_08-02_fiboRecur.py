# 한번 계산된 결과를 memoization 하기 위한 리스트 초기화
d = [0]* 100

# 피보나치 함수를 재귀함수로 구현 (top-down dynamic programming)
def fibo(x):
    # 종료 조건
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적 있는 경우
    if d[x] != 0 :
        return d[x]
    # 아직 계싼되지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    d[x] = fibo(x-1)+fibo(x-2)
    return d[x]

print(fibo(99))