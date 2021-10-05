def solution(price, money, count):
    for i in range(1,count+1) :
        money -= price*i
    return 0 if money > 0 else -money

print(solution(3,20,4))