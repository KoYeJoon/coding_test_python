from collections import deque

n = int(input())
k = int(input())
board = [[0]*n for _ in range(n)]

for i in range(k):
    row,col = map(int,input().split())
    board[row-1][col-1] = 1

l = int(input())
rotate_arr = deque()
for i in range(l):
    rot_time,rot = input().split()
    rotate_arr.append([int(rot_time),rot])

dcol = (1,0,-1,0)
drow = (0,-1,0,1)


def change_direction(dir,c_dir):
    # left
    if c_dir == 'L':
        if dir == 3:
            return 0
        return dir+1

    # right
    if dir == 0:
        return 3
    return dir-1


def check(arr,snake):
    if arr[0]<0 or arr[0]>n-1 or arr[1]<0 or arr[1]>n-1 :
        return False

    for i in range(len(snake)):
        if arr == snake[i]:
            return False
    return True


snake = deque([[0,0]])
time = 0
rot_time,rot = rotate_arr.popleft()
direction = 0

while True:
    time += 1
    new_x,new_y = snake[0][0]+drow[direction],snake[0][1] + dcol[direction]
    if not check([new_x,new_y],snake):
        break

    snake.appendleft([new_x,new_y])
    if board[new_x][new_y]:
        board[new_x][new_y] = 0
    else :
        snake.pop()

    if time == rot_time :
        direction = change_direction(direction,rot)
        if len(rotate_arr)>0 :
            rot_time,rot = rotate_arr.popleft()

print(time)