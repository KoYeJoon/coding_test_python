# def solution(board):
#     stride = 1
#     i=0
#     j=0
#     while stride <= len(board) and stride <= len(board[0]) :
#         flag=0
#         for l in range(i,i+stride):
#             for k in range(j,j+stride):
#                 if board[l][k]==0 :
#                     flag=1
#                 elif l==i+stride-1 and k==j+stride-1:
#                     if board[l][k]==1 :
#                         flag=2
#                     else :
#                         flag=1
#             if flag==1:
#                 break
#         if flag==1 :
#             i += 1
#         elif flag== 2:
#             if stride == len(board) or stride == len(board[0]):
#                 return stride ** 2
#             stride += 1
#             i=0
#             j=0
#
#         if i+stride > len(board):
#             i=0
#             j+=1
#         if j+stride>len(board[0]) :
#             break
#
#     return (stride-1) ** 2

def solution(board):
    answer = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if i==0 or j==0:
                continue
            if board[i][j] != 0:
                board[i][j] = min(board[i-1][j-1],min(board[i-1][j],board[i][j-1]))+1


    for i in range(len(board)):
        answer.append(max(board[i]))
    return max(answer)**2


print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
