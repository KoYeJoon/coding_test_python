'''
5
8 3 7 9 2
3
5 7 9
'''
# import sys
# n = int(sys.stdin.readline().rstrip())
# things = list(map(int,sys.stdin.readline().rstrip().split()))
# things.sort()
#
# m = int(sys.stdin.readline().rstrip())
# find_things = list(map(int,sys.stdin.readline().rstrip().split()))
#
#
# def binary_search(arr, start, end, target):
#     while start<=end :
#         mid = (start+end)//2
#         if arr[mid] == target:
#             return True
#         elif arr[mid]  < target :
#             start = mid + 1
#         else :
#             end = mid-1
#
#     return False
#
#
# for i in find_things :
#     if binary_search(things,0,n-1,i) :
#         print("yes", end = " ")
#     else :
#         print("no", end = " ")


# 계수 정렬
'''
n = int(input())
array = [0] * 1000001

for i in input().split() :
    array[int(i)] = 1

m = int(input())
x = list(map(int,input().split()))


for i in x :
    if array[i] == 1 :
        print('yes', end = ' ')
else:
    print('no', end = ' ')
'''


# 집합 이용
n = int(input())
array = set(map(int,input().split()))

m = int(input())
x = list(map(int,input().split()))

for i in x:
    if x in array:
        print('yes', end = ' ')
else:
    print('no', end = ' ')
