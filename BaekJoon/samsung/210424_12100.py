import sys

input = sys.stdin.readline

n = int(input())
game = []
for i in range(n):
    game.append(list(map(int,input().split())))

def found_max(game_map):
    max_num=0
    for i in range(n):
        if max_num < max(game_map[i]) :
            max_num = max(game_map[i])
    return max_num


def go_left(count,old_map) :
    new_map = [[0 for _ in range(n)] for _ in range(n)]
    if count > 5:
        return found_max(old_map)
    for i in range(n):
        temp = 0
        flag = 0
        new_map_j = 0
        for j in range(n):
            if temp == 0 or old_map[i][j] == 0 :
                if old_map[i][j] != 0 :
                    temp = old_map[i][j]
                continue

            if flag == 0:
                if temp == old_map[i][j] :
                    new_map[i][new_map_j] = temp*2
                    flag = 1
                else :
                    new_map[i][new_map_j] = temp
                # 다음 값은 다음에 저장되도록
                new_map_j += 1
                temp = old_map[i][j]
            else:
                temp = old_map[i][j]
                flag = 0

        if flag == 0 and temp != 0:
            new_map[i][new_map_j] = temp



    return go_everywhere(count+1,new_map)



def go_right(count, old_map) :
    new_map = [[0 for _ in range(n)] for _ in range(n)]
    if count > 5:
        return found_max(old_map)
    for i in range(n):
        temp = 0
        flag = 0
        new_map_j = n-1
        for j in range(n-1,-1,-1):
            if temp == 0 or old_map[i][j] == 0:
                if old_map[i][j] != 0 :
                    temp = old_map[i][j]
                continue

            if flag == 0:
                if temp == old_map[i][j] :
                    new_map[i][new_map_j] = temp*2
                    flag = 1
                else :
                    new_map[i][new_map_j] = temp
                # 다음 값은 다음에 저장되도록
                new_map_j -= 1
                temp = old_map[i][j]
            else:
                temp = old_map[i][j]
                flag = 0
        if flag == 0 and temp != 0:
            new_map[i][new_map_j] = temp

    return go_everywhere(count+1,new_map)


def go_up(count, old_map) :
    new_map = [[0 for _ in range(n)] for _ in range(n)]
    if count > 5:
        return found_max(old_map)
    for i in range(n):
        temp = 0
        flag = 0
        new_map_j = 0
        for j in range(n):
            if temp == 0 or old_map[j][i] == 0:
                if old_map[j][i] != 0 :
                    temp = old_map[j][i]
                continue

            if flag == 0:
                if temp == old_map[j][i] :
                    new_map[new_map_j][i] = temp*2
                    flag = 1
                else :
                    new_map[new_map_j][i] = temp
                # 다음 값은 다음에 저장되도록
                new_map_j += 1
                temp = old_map[j][i]
            else:
                temp = old_map[j][i]
                flag = 0

        if flag == 0 and temp != 0:
            new_map[new_map_j][i] = temp

    return go_everywhere(count+1,new_map)


def go_down(count,old_map):
    new_map = [[0 for _ in range(n)] for _ in range(n)]
    if count > 5:
        return found_max(old_map)
    for i in range(n):
        temp = 0
        flag = 0
        new_map_j = n-1
        for j in range(n-1,-1,-1):
            if temp == 0 or old_map[j][i] == 0:
                if old_map[j][i] != 0 :
                    temp = old_map[j][i]
                continue

            if flag == 0:
                if temp == old_map[j][i] :
                    new_map[new_map_j][i] = temp*2
                    flag = 1
                else :
                    new_map[new_map_j][i] = temp
                # 다음 값은 다음에 저장되도록
                new_map_j -= 1
                temp = old_map[j][i]
            else:
                temp = old_map[j][i]
                flag = 0
        if flag == 0 and temp != 0:
            new_map[new_map_j][i] = temp

    return go_everywhere(count+1,new_map)


dp = []
def go_everywhere(count,old_map):
    dp.append(max(go_left(count,old_map),go_right(count,old_map),go_up(count,old_map),go_down(count,old_map)))
    return max(dp)


print(go_everywhere(1,game))
