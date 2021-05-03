import sys
input = sys.stdin.readline
n,m,x,y,k = map(int,input().split())
game = []
for i in range(n):
    game.append(list(map(int,input().split())))

command = list(map(int,input().split()))
# 동, 서, 바닥, 위, 앞, 뒤
map_dice = [0,0,0,0,0,0]

# 남, 동, 서, 북 (4로 나눈 나머지가 0인 경우가 남)
dx = (1,0,0,-1)
dy = (0,1,-1,0)

def dice_face_change(num,old_dice) :
    new_dice = [0 for _ in range(6)]
    # 남
    if num == 0:
        new_dice[0] = old_dice[0]
        new_dice[1] = old_dice[1]
        new_dice[2] = old_dice[4]
        new_dice[3] = old_dice[5]
        new_dice[4] = old_dice[3]
        new_dice[5] = old_dice[2]
    # 동
    elif num == 1 :
        new_dice[0] = old_dice[3]
        new_dice[1] = old_dice[2]
        new_dice[2] = old_dice[0]
        new_dice[3] = old_dice[1]
        new_dice[4] = old_dice[4]
        new_dice[5] = old_dice[5]
    # 서
    elif num == 2:
        new_dice[0] = old_dice[2]
        new_dice[1] = old_dice[3]
        new_dice[2] = old_dice[1]
        new_dice[3] = old_dice[0]
        new_dice[4] = old_dice[4]
        new_dice[5] = old_dice[5]
    # 북
    else :
        new_dice[0] = old_dice[0]
        new_dice[1] = old_dice[1]
        new_dice[2] = old_dice[5]
        new_dice[3] = old_dice[4]
        new_dice[4] = old_dice[2]
        new_dice[5] = old_dice[3]

    return new_dice

for i in range(k) :
    pos_x = x+dx[command[i]%4]
    pos_y = y+dy[command[i]%4]
    if pos_x > n-1 or pos_y > m-1 or pos_x < 0 or pos_y < 0:
        continue

    # 주사위면 바꾸기
    map_dice = dice_face_change(command[i]%4, map_dice)
    # 윗면 출력
    print(map_dice[3])
    if game[pos_x][pos_y] == 0:
        game[pos_x][pos_y] = map_dice[2]
    else :
        map_dice[2] = game[pos_x][pos_y]
        game[pos_x][pos_y] = 0

    # 좌표 업데이트
    x = pos_x
    y = pos_y