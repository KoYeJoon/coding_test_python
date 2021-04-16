'''
4 6
19 14 10 17
'''
import sys
n,m = map(int, sys.stdin.readline().rstrip().split())
dduck = list(map(int,sys.stdin.readline().rstrip().split()))
total_dduck = sum(dduck)

start = 0
end = max(dduck)
result = 0
while start<=end :
    mid = (start+end)//2
    cut_dduck = list(map(lambda x : x-mid if x>mid else 0, dduck))
    add_dduck = sum(cut_dduck)
    if add_dduck < m :
        end = mid-1
    else:
        result = mid
        start = mid+1

print(result)



# n,m = list(map(int,input().split(' ')))
# array = list(map(int,input().split()))
#
# start = 0
# end = max(array)
#
# # 이진 탐색 수행
# result = 0
# while start<=end :
#     total = 0
#     mid = (start+end) // 2
#     for x in array :
#         # 잘랐을 때 떡의 양 계산
#         if x > mid :
#             total += x-mid
#     # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
#     if total < m :
#         end = mid - 1
#     # 떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
#     else:
#         result = mid	# 최대한 덜 짤랐을 때가 정답이므로, 여기에서 result에 기록한다.
#         start = mid + 1
#
# # 정답출력
# print(result)