def possible(n,stones,k):
    stones = list(stones)
    if max(stones) < n:
        return False
    temp = 0
    for i in range(len(stones)):
        stones[i] -= n
        if stones[i]<0 :
            temp += 1
            if temp>=k :
                return False
        else :
            temp = 0
    return True

def solution(stones,k):
    left = 0
    right = 200000001
    mid = (left+right)//2

    while left< right :
        mid = (left+right)//2
        if left == mid or right==mid:
            break
        if possible(mid,stones,k) :
            left = mid
        else :
            right = mid
    return mid

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))