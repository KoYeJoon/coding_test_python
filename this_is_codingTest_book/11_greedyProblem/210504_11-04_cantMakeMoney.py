import sys
input = sys.stdin.readline

n = int(input())
coin_list = list(map(int,input().split()))

coin_list.sort()

coin = 1
for i in coin_list:
    if i > coin :
        break
    coin += i

print(coin)
