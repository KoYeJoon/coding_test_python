def solution(gems):
    gems_dir = {}

    for gem in gems:
        if gem in gems_dir:
            gems_dir[gem] += 1
        else :
            gems_dir[gem]= 1

    left = 0
    right = 0
    gems_dir_keys = list(gems_dir.keys())

    while left < len(gems) and right < len(gems):
        buy_gem = []
        if gems_dir[gems[left]] >1 :
            gems_dir[gems[left]] -= 1
            left += 1

        buy_gem = gems[left-1:right]
        if gem[left] == gem[left-1]:
            left += 1

        if set(gems_dir_keys) == set(buy_gem) :
            break
        else :
            right += 1

    return [left,right]

print(solution(["AA", "AB", "AC", "AA", "AC"]))