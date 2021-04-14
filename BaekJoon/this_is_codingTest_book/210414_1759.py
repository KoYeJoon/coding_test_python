import itertools
import sys

vowels = ['a','e','i','o','u']
L,C = map(int, input().split())
data = sys.stdin.readline().rstrip().split()
data.sort()

combi = list(itertools.combinations(data,L))
for i in combi :
    count = 0
    for j in i :
        if j in vowels :
            count += 1
    # 모음 1개 이상, 자음 2개 이상
    if count > 0 and L-count > 1:
        print(''.join(i))

# from itertools import combinations
#
# vowels = ('a','e','i','o','u')
# l,c = map(int,input().split(' '))
# array = input().split(' ')
# array.sort()
#
# for password in combinations(array,l) :
#     count = 0
#     for i in password :
#         if i in vowels :
#             count += 1
#     if count >= 1 and count <= l-2 :
#         print(''.join(password))