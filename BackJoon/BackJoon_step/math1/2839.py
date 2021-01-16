def sugar(N) :
    for y in range( (N//3)+1) :
        for x in range( (N//5)+1 ) :
            if ((5*x + 3*y) == N) :
                return x+y
            
    return -1

N = int(input()) #배달해야할 설탕 킬로그램         
print(sugar(N))
