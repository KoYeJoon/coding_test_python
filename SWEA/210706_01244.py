import copy
T = int(input())

def dfs(list_arr,start,cnt):
    arr = copy.deepcopy(list_arr)
    flag = 1

    if cnt == change_num :
        tmp = int(''.join(list(map(str,arr))))
        global ret
        if ret < tmp :
            ret = tmp
        return

    for i in range(start,len_n-1):
        for j in range(i+1,len_n):
            if arr[i] <= arr[j]:
                flag = 0
                arr[i],arr[j] = arr[j],arr[i]
                dfs(arr,i,cnt+1)
                arr[i],arr[j] = arr[j],arr[i]
    if flag :
        arr[-1], arr[-2] = arr[-2], arr[-1]
        dfs(arr, start,cnt+1)


# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, change_num = map(int,input().split())
    list_n = list(map(int,str(n)))
    len_n = len(str(n))
    global ret
    ret = 0
    dfs(list_n,0,0)
    print(f'#{test_case}',end=' ')
    print(ret)
