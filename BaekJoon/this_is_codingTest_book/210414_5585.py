money = int(input())
coin = [500,100,50,10,5,1]
count,i = 0,0
money = 1000 - money

while money > 0 :
    if money > coin[i] :
        count += 1
        money -= coin[i]
    elif money == coin[i]:
        count += 1
        break
    else :
        i += 1

print(count)

# n = int(input())
# count = 0
# coin_types = [500,100,50,10,5,1]
# n = 1000-n
#
# for coin in coin_types :
#     count += n // coin
#     n %= coin
#
# print(count)