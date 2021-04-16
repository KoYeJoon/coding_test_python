n,m = map(int,input().split())
x,y,direction = map(int,input().split())

map_list = []
for i in range(n) :
    map_list.append(list(map(int,input().split())))

# 0 : 북, 1 : 동, 2: 남, 3 : 서
dx = [-1,0,1,0]
dy = [0,1,0,-1]
mark = [[0 for i in range(m)] for j in range(n)]
turn_count = 0
while True :
    mark[x][y] = 1
    # 왼쪽으로 회전
    direction -= 1
    if direction < 0 :
        direction = 3

    # 가보지 않은 칸이 있는 경우
    if map_list[x+dx[direction]][y+dy[direction]] == 0 and mark[x+dx[direction]][y+dy[direction]]==0 :
        x += dx[direction]
        y += dy[direction]
        turn_count = 0

    # 해당 방향으로 다 가본 경우
    else :
        turn_count += 1

    if turn_count == 4 :
        # 뒤로 갈 수 있는 경우
        if map_list[x+dx[direction-2]][y+dy[direction-2]] == 0 :
            x += dx[direction-2]
            y += dy[direction-2]
            turn_count = 0
        # 뒤로 갈 수 없는 경우
        else:
            break

count = 0
for i in range(n):
    count += mark[i].count(1)

print(count)

# n,m = map(int, input().split())
#
# # 방문한 위치를 저장하기 위함
# d = [[0]*m for _ in range(n)]
# # 캐릭터의 x,y 좌표와 방향 입력받기
# x,y,direction = map(int,input().split())
# d[x][y] = 1 # 현재 좌표 방문 처리
#
# # 전체 맵 정보 받기
# array = []
# for i in range(n) :
#     array.append(list(map(int, input().split())))
#
# # 동, 서, 남, 북 방향 정의
# dx = [-1, 0, 1, 0]
# dy = [0,1,0,-1]
#
# # 왼쪽으로 회전
# def turn_left() :
#     global direction
# direction -= 1
# if direction == -1 :
#     direction = 3
#
# # 시뮬레이션 시작
# count = 1
# turn_time = 0
# while True :
#     # 왼쪽으로 회전
#     turn_left()
#     nx = x + dx[direction]
#     dy = y + dy[direction]
#     # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
#     if d[nx][ny] == 0 and array[nx][ny] == 0:
#         d[nx][ny] = 1
#         x = nx
#         y = ny
#         count += 1
#         turn_time = 0
#         continue
#     # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
#     else :
#         turn_time += 1
#
#     # 네 방향 모두 갈 수 없는 경우
#     if turn_time == 4 :
#         nx = x - dx[direction]
#         ny = y - dy[direction]
#         # 뒤로 갈 수 있다면 이동하기
#         if array[nx][ny] == 0:
#             x = nx
#             y = ny
#         # 뒤가 바다로 막힌 경우
#         else :
#             break
#
#         turn_time = 0
#
#     # 정답 출력
# print(count)