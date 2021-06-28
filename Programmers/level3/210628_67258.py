def solution(gems):
    buy_gem_dic = {}
    num_gem = len(set(gems))
    left = 1
    right = len(gems)
    temp_left = 1
    temp_right = 0

    while temp_left-1 < len(gems) and temp_right-1 < len(gems):
        if num_gem == len(buy_gem_dic) :
            if right-left > temp_right - temp_left:
                left = temp_left
                right = temp_right

            if right-(left-1) == num_gem :
                break

            if buy_gem_dic[gems[temp_left-1]] == 1:
                del buy_gem_dic[gems[temp_left-1]]
            else :
                buy_gem_dic[gems[temp_left-1]] -= 1
            temp_left += 1

        else :
            if temp_right < len(gems):
                if gems[temp_right] in buy_gem_dic.keys() :
                    buy_gem_dic[gems[temp_right]] += 1
                else :
                    buy_gem_dic[gems[temp_right]] = 1
            temp_right += 1

    return [left,right]


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))