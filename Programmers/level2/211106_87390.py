def solution(n, left, right):
    left_row = left// n + 1
    left_col = left % n
    right_row = right // n + 1
    right_col = right % n
    arr2d = [[max(i,j) for i in range(1,n+1)] for j in range(left_row,right_row+1)]

    answer = [data for inner_list in arr2d for data in inner_list]
    return answer[left_col:(right_row-left_row)*n+right_col+1]

print(solution(	4, 7, 14))