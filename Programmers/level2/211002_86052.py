def dfs(grid,init_path):
    # down, right, up, left
    drow = [1,0,-1,0]
    dcol = [0,1,0,-1]
    visited = [[[0] * 4 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for i in range(len(init_path)):
        stack = []
        original_path = init_path[i]
        stack.append(original_path)
        count = 0

        while stack :
            count += 1
            pos = stack.pop()
            pos_row = pos[0]
            pos_col = pos[1]
            pos_dir = pos[2]

            visited[pos_row][pos_col][pos_dir] = 1

            if grid[pos_row][pos_col] == 'R' :
                pos_dir = (pos_dir+5)%4
                nr = pos_row + drow[pos_dir]
                nc = pos_col + dcol[pos_dir]
            elif grid[pos_row][pos_col]=='L':
                pos_dir = (pos_dir+7)%4
                nr = pos_row + drow[pos_dir]
                nc = pos_col + dcol[pos_dir]
            else :
                nr = pos_row + drow[pos_dir]
                nc = pos_col + dcol[pos_dir]

            if nr >= row:
                nr = 0
            elif nr < 0:
                nr = len(grid) - 1
            if nc >= col:
                nc = 0
            elif nc < 0:
                nc = len(grid[0]) - 1

            if original_path[0] == nr and original_path[1] == nc and original_path[2]==pos_dir:
                answer.append(count)
                break

            if not visited[nr][nc][pos_dir] :
                stack.append([nr,nc,pos_dir])


def solution(grid):
    global answer
    global row,col
    row = len(grid)
    col = len(grid[0])

    answer = []
    init_pos = []
    dirs = [0,1,2,3]
    for i in range(row):
        for j in range(col) :
            for dir in dirs :
                init_pos.append([i,j,dir])
    dfs(grid,init_pos)
    answer.sort()
    return answer


print(solution(["SL","LR"]))