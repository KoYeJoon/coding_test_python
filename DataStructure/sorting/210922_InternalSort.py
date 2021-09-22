array = [7,5,9,0,3,1,6,2,4,8]

def insertionSort(arr):
    for i in range(1,len(arr)):
        for j in range(i):
            if arr[j]>arr[i] :
                arr[j],arr[i] = arr[i],arr[j]

    return arr

# print(insertionSort(array))


def bubbleSort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-1-i):
            if arr[j+1]<arr[j]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

#print(bubbleSort(array))


def selectionSort(arr):
    for i in range(len(array)):
        min_index = i	# 가장 작은 원소의 인덱스
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j] :
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i] # 스와프
    return arr

#print(selectionSort(array))

def quick_sort(arr, start, end) :
    if start >= end :	# 원소가 1개인 경우 종료
        return
    pivot = start # pivot 은 첫 번째 원소
    left = start + 1
    right = end
    #print(arr)
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and arr[left] <= arr[pivot] :
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and arr[right] >= arr[pivot] :
            right -= 1

        if left > right :	# 엇갈렸다면 짝은 데이터와 피벗 교체
            arr[right], arr[pivot] = arr[pivot] , arr[right]
        else :			# 엇갈리지 않았다면 작은 데이터와 큰 데이터의 교체
            arr[left], arr[right] = arr[right], arr[left]

        # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
        quick_sort(arr,start, right-1)
        quick_sort(arr,right+1, end)

    return arr

#print(quick_sort(array, 0, len(array)-1))

def quick_sort_python(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[0]
    tail = arr[1:]
    left_side = [x for x in tail if x<=pivot]
    right_side = [x for x in tail if x>pivot]

    return quick_sort_python(left_side)+[pivot]+quick_sort_python(right_side)

#print(quick_sort_python(array))

def mergesort(arr):
    if len(arr)<=1 :
        return arr
    mid = len(arr)//2
    left_side = arr[:mid]
    right_side = arr[mid:]
    if len(left_side)>1:
        left_side = mergesort(left_side)
    if len(right_side)>1:
        right_side= mergesort(right_side)

    res = []
    while left_side and right_side :
        if left_side[0] < right_side[0]:
            res.append(left_side.pop(0))
        else :
            res.append(right_side.pop(0))

    return res+(left_side or right_side)

#print(mergesort(array))

import heapq
def heapsort(arr):
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]

#print(heapsort(array))

array2 = [1300,326,453,608,835,751,435,704,690]
def radixSort(arr):
    max_len = len(str(max(arr)))
    for l in range(max_len):
        digit = [0]*10
        temp = [0]*len(arr)
        for a in arr :
            digit[(a//(10**l))%10]+=1

        for i in range(9):
            digit[i+1] += digit[i]

        for i in reversed(range(len(arr))):
            temp[digit[(arr[i]//(10**l))%10]-1] = arr[i]
            digit[(arr[i]//(10**l))%10] -= 1

        arr = temp

    return arr


print(radixSort(array2))