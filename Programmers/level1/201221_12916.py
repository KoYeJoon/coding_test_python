def solution(s):
    answer = True
    countP = 0
    countY = 0
    for a in s :
        if a in ['p','P'] :
            countP = countP + 1
            answer = False
        if a in ['y','Y'] :
            countY = countY + 1
            answer=False

    if countP != 0 and countY != 0:
        if(countP==countY) :
            answer=True
    return answer

s="Pyy"
print(solution(s))