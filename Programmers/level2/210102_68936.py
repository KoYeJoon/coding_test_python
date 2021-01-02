def solution(arr):
    answer = [0,0]
    zero_count = 0
    one_count = 0
    for i in range(len(arr)):
        zero_count += arr[i].count(0)
        one_count += arr[i].count(1)
    arr_len = len(arr)*len(arr[0])
    if zero_count == arr_len :
        return [1,0]
    elif one_count==arr_len:
        return [0,1]

    else :
        row_len_div_2 = len(arr)//2
        col_len_div_2 = len(arr[0])//2
        if row_len_div_2 == 0 or col_len_div_2 ==0:
            return [zero_count,one_count]
        else:
            for i in range(0,len(arr),row_len_div_2):
                for j in range(0,len(arr[0]),col_len_div_2):
                    temp_arr=[]
                    for k in range(i,i+row_len_div_2):
                        temp_arr.append(arr[k][j:j+len(arr)//2])
                    temp = solution(temp_arr)
                    answer[0] += temp[0]
                    answer[1] += temp[1]
    return answer


# import numpy as np
#
# def solution(arr):
#     # 재귀함수 구현
#     def fn(a):
#         if np.all(a == 0): return np.array([1, 0])
#         if np.all(a == 1): return np.array([0, 1])
#         n = a.shape[0]//2
#         return fn(a[:n, :n]) + fn(a[n:, :n]) + fn(a[:n, n:]) + fn(a[n:, n:])
#
#     # 결과 리턴
#     return fn(np.array(arr))

print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))