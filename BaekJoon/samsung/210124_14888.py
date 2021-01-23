from sys import stdin
import itertools

n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))

# +,-,x,/ -> n-1개 주어짐
cal = list(map(int, stdin.readline().split()))
new_cal = []
new_cal += list('+'*cal[0]) + list('-'*cal[1]) + list('*'*cal[2]) + list('/'*cal[3])

max_n = -9999999999
min_n = 9999999999

cal_per = set(itertools.permutations(new_cal,n-1))
def calculator(x,y,c):
    if c=='+':
        return x+y
    elif c == '-':
        return x-y
    elif c=='*':
        return x*y
    else :
        if x< 0 :
            return -((-x)//y)
        return x//y

for i in cal_per:
    result = 0
    for j in range(len(i)) :
        if j==0:
            result = calculator(a[j],a[j+1],i[j])
        else :
            result = calculator(result,a[j+1],i[j])

    if result < min_n :
        min_n = result
    if result > max_n :
        max_n = result

print(max_n)
print(min_n)


# from sys import stdin
#
# n = int(stdin.readline())
# a = list(map(int, stdin.readline().split()))
#
# # +,-,x,/ -> n-1개 주어짐
# cal = list(map(int, stdin.readline().split()))
#
# max_n = -9999999999
# min_n = 9999999999
#
# def calculator(plus,minus,mul,div,arr,result,idx) :
#     global max_n
#     global min_n
#     if idx == n:
#         if result > max_n :
#             max_n = result
#         if result < min_n:
#             min_n = result
#         return
#
#     if plus > 0 :
#         calculator(plus-1,minus,mul,div,arr,result + arr[idx],idx+1)
#
#     if minus > 0 :
#         calculator(plus, minus-1, mul , div, arr,result - arr[idx],idx+1)
#
#     if mul > 0:
#         calculator(plus,minus,mul-1,div,arr,result * arr[idx],idx+1)
#
#     if div > 0:
#         if result < 0 :
#             tmp = -((-result)//arr[idx])
#         else :
#             tmp = result//arr[idx]
#         calculator(plus,minus,mul,div-1,arr,tmp,idx+1)
#
#
# calculator(cal[0],cal[1],cal[2],cal[3],a,a[0],1)
#
# print(max_n)
# print(min_n)