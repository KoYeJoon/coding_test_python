import math

m,n = map(int, input().split())
num = set(range(2,n+1))

for i in range(2,int(math.sqrt(n))+1):
    if i in num :
        num-= set(range(2*i,n+1,i))

list_num = list(num)
list_num.sort()
for i in list_num :
    if i >= m and i <= n:
        print(i)

# import math
#
# # M,N 입력 받기
# m,n = map(int, input().split())
# array = [True for i in range(1000001)]
# array[1] = 0 #1은 소수가 아니다
#
# for i in range(2, int(math.sqrt(n))+1) :
#     if array[i]:	#i가 소수인 경우(남은 수인 경우)
#         j=2
#     while i*j <= n:
#         array[i*j] = False
#         j+=1
#
# # M부터 N까지의 모든 소수 출력
# for i in range(m,n+1) :
#     if array[i] :
#         print(i)