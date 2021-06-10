def solution(lottos, win_nums):
    correct_n = 0
    zero_count = lottos.count(0)
    for i in lottos :
        if i in win_nums :
            correct_n += 1

    answer = [7-(correct_n+zero_count) if correct_n+zero_count>1 else 6 , 7-correct_n if correct_n>1 else 6]
    return answer