def goup(map,posR,posB,count):
    #up
    new_R=list(posR)
    new_B=list(posB)
    for i in range(posR[0]-1,-1,-1) :
        if map[i][posR[1]] == 'O':
            for j in range(posB[0]-1,-1,-1):
                if map[j][posB[1]] == 'O' :
                    return 0
            return count
        elif map[i][posR[1]] != '.':
            map[posR[0]][posR[1]] = '.'
            map[i+1][posR[1]] = 'R'
            new_R[0]=i+1
            break

    for i in range(posB[0]-1,0,-1) :
        if map[i][posB[1]] != '.':
            map[posB[0]][posB[1]] = '.'
            map[i+1][posB[1]] = 'B'
            new_B[0]=i+1
            break

    return findMap(map,new_R,new_B,count+1,1)


def godown(map,posR,posB,count):
    #down
    new_R=list(posR)
    new_B=list(posB)
    for i in range(posR[0]+1,n) :
        if map[i][posR[1]] == 'O':
            for j in range(posB[0]+1,n):
                if map[j][posB[1]] == 'O' :
                    return 0
            return count
        elif map[i][posR[1]] != '.':
            map[posR[0]][posR[1]] = '.'
            map[i-1][posR[1]] = 'R'
            new_R[0]=i-1
            break

    for i in range(posB[0]+1,n) :
        if map[i][posB[1]] != '.':
            map[posB[0]][posB[1]] = '.'
            map[i-1][posB[1]] = 'B'
            new_B[0]=i-1
            break

    return findMap(map,new_R,new_B,count+1,2)


def goleft(map,posR,posB,count):
    #left
    new_R=list(posR)
    new_B=list(posB)
    for i in range(posR[1]-1,-1,-1) :
        if map[posR[0]][i] == 'O':
            for j in range(posB[1]-1,-1,-1):
                if map[posB[0]][j] == 'O' :
                    return 0
            return count
        elif map[posR[0]][i] != '.':
            map[posR[0]][posR[1]] = '.'
            map[posR[0]][i+1] = 'R'
            new_R[1]=i+1
            break


    for i in range(posB[1]-1,-1,-1) :
        if map[posB[0]][i] != '.':
            map[posB[0]][posB[1]] = '.'
            map[posB[0]][i+1] = 'B'
            new_B[1]=i+1
            break

    return findMap(map,new_R,new_B,count+1,3)


def goright(map,posR,posB,count):
    #right
    new_R=list(posR)
    new_B=list(posB)
    for i in range(posR[1]+1,m) :
        if map[posR[0]][i] == 'O':
            for j in range(posB[1]+1,m):
                if map[posB[0]][j] == 'O' :
                    return 0
            return count
        elif map[posR[0]][i] != '.':
            map[posR[0]][posR[1]] = '.'
            map[posR[0]][i-1] = 'R'
            new_R[1]=i-1
            break

    for i in range(posB[1]+1,m) :
        if map[posB[0]][i] != '.':
            map[posB[0]][posB[1]] = '.'
            map[posB[0]][i-1] = 'B'
            new_B[1]=i-1
            break

    return findMap(map,new_R,new_B,count+1,4)


import copy
def findMap(tempmap,posR,posB,count,pos):
    if count > 10:
        return 0
    if pos ==0 :
        map = copy.deepcopy(tempmap)
        a=goleft(map,posR,posB,count)
        map = copy.deepcopy(tempmap)
        b=goright(map,posR,posB,count)
        map = copy.deepcopy(tempmap)
        c=goup(map,posR,posB,count)
        map = copy.deepcopy(tempmap)
        d=godown(map,posR,posB,count)
    elif pos == 1:
        map = copy.deepcopy(tempmap)
        a=goleft(map,posR,posB,count)
        map = copy.deepcopy(tempmap)
        b=goright(map,posR,posB,count)
        c=0
        map = copy.deepcopy(tempmap)
        d=godown(map,posR,posB,count)
    elif pos == 2:
        map = copy.deepcopy(tempmap)
        a=goleft(map,posR,posB,count)
        map = copy.deepcopy(tempmap)
        b=goright(map,posR,posB,count)
        map = copy.deepcopy(tempmap)
        c=goup(map,posR,posB,count)
        d=0
    elif pos == 3:
        a=0
        map = copy.deepcopy(tempmap)
        b=goright(map,posR,posB,count)
        map = copy.deepcopy(tempmap)
        c=goup(map,posR,posB,count)
        map = copy.deepcopy(tempmap)
        d=godown(map,posR,posB,count)
    elif pos == 4:
        map = copy.deepcopy(tempmap)
        a=goleft(map,posR,posB,count)
        b=0
        map = copy.deepcopy(tempmap)
        c=goup(map,posR,posB,count)
        map = copy.deepcopy(tempmap)
        d=godown(map,posR,posB,count)

    if a==0 and b==0 and c==0 and d==0 :
        return 0
    temp = [a,b,c,d]
    return min(filter(lambda x : x>0, temp))



n,m= map(int,input().split())
bigmap = []
for i in range(n):
    inputStr = input()
    arr = list(inputStr)
    bigmap.append(arr)

posR = []
posB = []
for i in range(n) :
    for j in range(m) :
        if bigmap[i][j] == 'R' :
            posR.append(i)
            posR.append(j)
        elif bigmap[i][j] == 'B' :
            posB.append(i)
            posB.append(j)
a = findMap(bigmap,posR,posB,1,0)

if a==0 :
    print(-1)
else:
    print(a)