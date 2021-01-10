import itertools
def solution(nums):
    answer = 0
    combi_list = list(itertools.combinations(nums,3))
    sum_nums = sum(nums)+1
    sosu = set(range(2,sum_nums))
    for i in range(2,sum_nums) :
        if i in sosu :
            sosu -= set(range(2*i,sum_nums,i))
    for i in range(len(combi_list)) :
        temp = sum(combi_list[i])
        if temp in sosu :
            answer += 1
    return answer

print(solution([1,2,3,4]))