def lomuto_partitioning(arr,l,r):
    p = arr[l]
    s = l
    for i in range(l+1,r+1) :
        if arr[i]<p :
            s+=1
            arr[s],arr[i] = arr[i],arr[s]

    arr[l],arr[s] = arr[s],arr[l]
    return s

def hoare_partitioning(arr,l,r):
    p = arr[l]
    i = l
    j = r
    while i<j :
        while arr[i]<p : i+=1
        while arr[j]>p : j-=1
        arr[i],arr[j] = arr[j],arr[i]

    if i > j : # 엇갈렸다면 피봇과 작은 데이터 교체
        arr[l],arr[j] = arr[j],arr[l]
    else :			# 엇갈리지 않았다면 작은 데이터와 큰 데이터의 교체
        arr[i],arr[j] = arr[j],arr[i]

    return j

def quicksort(arr,l,r):
    if l<r :
        #s = lomuto_partitioning(arr,l,r)
        s=hoare_partitioning(arr,l,r)
        quicksort(arr,l,s)
        quicksort(arr,s+1,r)
    return arr

arr = [3,29,30,24,39,100,2,50]
print(quicksort(arr,0,len(arr)-1))