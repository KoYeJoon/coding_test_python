def solution(nums):
    len_nums = len(nums)//2
    set_nums= set(nums)
    len_set_nums = len(set_nums)
    if len_set_nums < len_nums :
        return len_set_nums
    return len_nums