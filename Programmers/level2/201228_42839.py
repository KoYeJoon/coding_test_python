import itertools
def solution(numbers):
    answer = 0
    nPr = []
    for i in range(1,len(numbers)+1):
        nPr += itertools.permutations(numbers,i)

    temp = set()
    for i in range(len(nPr)) :
        temp.add(''.join(nPr[i]))

    list_num = set(map(int,temp))
    max_num = set(range(2,max(list_num)+1))
    for i in range(2,max(list_num)+1):
        if i in max_num :
            max_num -= set(range(2*i,max(list_num)+1,i))

    for i in list_num :
        if i in max_num :
            answer+=1
    return answer

print(solution("011"))

arr = ['1','2','3']
print(list(itertools.combinations(arr,2)))