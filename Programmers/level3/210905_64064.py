answer = []
def dfs(ban_dict, ban_ids, idx, id_set):
    if len(ban_ids) == idx :
        if set(id_set) not in answer:
            answer.append(set(id_set))
        return

    now = ban_ids[idx]
    for i in range(len(ban_dict[ban_ids[idx]])) :
        if ban_dict[now][i] in id_set :
            continue
        id_set.append(ban_dict[now][i])
        dfs(ban_dict,ban_ids, idx+1, id_set)
        id_set.pop()


def solution(user_id, banned_id):
    banned_dict = {}

    for b in banned_id :
        banned_dict[b] = []

    for bi in banned_id :
        for ui in user_id :
            if len(bi) != len(ui):
                continue
            for idx in range(len(bi)) :
                if bi[idx] == '*':
                    continue
                if bi[idx] != ui[idx] :
                    break
            else :
                if ui not in banned_dict[bi]:
                    banned_dict[bi].append(ui)

    dfs(banned_dict,banned_id,0,[])

    return len(answer)


'''
from itertools import permutations
def check_id(combo_ids,banned_ids):
    for i in range(len(combo_ids)):
        if len(combo_ids[i]) != len(banned_ids[i]) :
            return False
        for j in range(len(combo_ids[i])):
            if banned_ids[i][j] == '*':
                continue
            if combo_ids[i][j] != banned_ids[i][j] :
                return False
    return True


def solution(user_id, banned_id):
    answer = []
    for ui in permutations(user_id,len(banned_id)):
        if check_id(ui,banned_id):
            if set(ui) not in answer :
                answer.append(set(ui))

    return len(answer)
'''
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["*rodo", "*rodo", "******"]))