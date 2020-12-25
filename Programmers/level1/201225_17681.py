#zfill과 rjust 정리
def solution(n, arr1, arr2):
    answer=[]
    for i in range(n):
        map1 = bin(arr1[i])[2:]
        map1_arr = list(map1.zfill(n))
        #map1_arr=list(map1.rjust(n,'0'))
        map2 = bin(arr2[i])[2:]
        map2_arr= list(map2.zfill(n))
        temp=""
        for j in range(n):
            if map1_arr[j]=='1' or map2_arr[j]=='1' :
                temp += "#"
            else :
                temp += " "
        answer.append(temp)
    return answer

print(solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]))