S = [1,2,3,5,6,7,8,9,10,11,12]
key = 3

def binary_search_recursive(low,high):
    if low > high :
        return -1
    mid = (low+high)//2
    if key == S[mid] :
        return mid
    elif key<S[mid]:
        return binary_search_recursive(low,mid-1)
    else:
        return binary_search_recursive(mid+1,high)

def binary_search_iterative(n,S,key):
    low = 0
    high = n-1
    location = -1
    while low <= high and location==-1:
        mid = (low+high)//2
        if key == S[mid] :
            location = mid
        elif key < S[mid]:
            high = mid-1
        else :
            low = mid + 1
    return location

print(binary_search_recursive(0,len(S)))
print(binary_search_iterative(len(S),S,key))