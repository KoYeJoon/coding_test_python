# def dfs(k, cnt, dungeons):
#     global answer,visited,n
#     if cnt > answer:
#         answer = cnt
#
#     for j in range(n):
#         if k >= dungeons[j][0] and not visited[j]:
#             visited[j] = 1
#             dfs(k - dungeons[j][1], cnt + 1, dungeons)
#             visited[j] = 0
#
# def solution(k, dungeons):
#     global n, visited, answer
#     n = len(dungeons)
#     visited = [0] * n
#     answer = 0
#     dfs(k, 0, dungeons)
#     return answer

def solution(k, dungeons):
    n = len(dungeons)
    answer = 0
    for i in range(n):
        stack = [i]
        path = []
        cnt = 0
        visited = [0] * n
        sleepy = k
        while stack :
            idx = stack.pop()
            if not visited[idx] and sleepy >= dungeons[idx][0]:
                sleepy -= dungeons[idx][1]
                cnt += 1
                path.append(idx)
                visited[idx]=1

            elif not visited[idx] and sleepy < dungeons[idx][0]:
                if len(path)>0 :
                    p = path.pop()
                    visited[p] = 0
                    sleepy += dungeons[p][1]
                    cnt -= 1


            for j in range(n):
                if not visited[j] and sleepy >= dungeons[j][0]:
                    stack.append(j)

            visited[idx]=0

        answer = max(answer, cnt)
    return answer



print(solution(80,[[80,20],[50,40],[30,10]]))