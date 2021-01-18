def goup(map,posR,posB,count):
    #up
    new_R=list(posR)
    new_B=list(posB)

    for i in range(posB[0]-1,-1,-1) :
        if map[i][posB[1]] == 'O' :
            return 0
        if map[i][posB[1]] != '.':
            new_B[0]=i+1
            break

    for i in range(posR[0]-1,-1,-1) :
        if map[i][posR[1]] == 'O':
            return count
        elif map[i][posR[1]] != '.':
            if posR[1] == posB[1] :
                if i+1 == new_B[0] :
                    if posR[0] > posB[0] :
                        new_B[0]=i+1
                        new_R[0]=i+2
                    else :
                        new_B[0]=i+2
                        new_R[0]=i+1
            else :
                new_R[0]=i+1
            break

    return findMap(map,new_R,new_B,count+1,1)


def godown(map,posR,posB,count):
    #down
    new_R=list(posR)
    new_B=list(posB)

    for i in range(posB[0]+1,n) :
        if map[i][posB[1]] == 'O' :
            return 0
        if map[i][posB[1]] != '.':
            new_B[0]=i-1
            break

    for i in range(posR[0]+1,n) :
        if map[i][posR[1]] == 'O':
            return count
        elif map[i][posR[1]] != '.':
            if posR[1] == posB[1] :
                if i-1 == new_B[0] :
                    if posR[0] > posB[0] :
                        new_B[0]=i-2
                        new_R[0]=i-1
                    else :
                        new_B[0]=i-1
                        new_R[0]=i-2
            else :
                new_R[0]=i-1
            break

    return findMap(map,new_R,new_B,count+1,2)


def goleft(map,posR,posB,count):
    #left
    new_R=list(posR)
    new_B=list(posB)

    for i in range(posB[1]-1,-1,-1) :
        if map[posB[0]][i] == 'O' :
            return 0
        if map[posB[0]][i] != '.':
            new_B[1]=i+1
            break

    for i in range(posR[1]-1,-1,-1) :
        if map[posR[0]][i] == 'O':
            return count
        elif map[posR[0]][i] != '.':
            if posR[0]==posB[0] :
                if i+1 == new_B[1] :
                    if posR[1]>posB[1]:
                        new_B[1] = i+1
                        new_R[1] = i+2
                    else :
                        new_B[1] = i+2
                        new_R[1] = i+1
            else:
                new_R[1]=i+1
            break

    return findMap(map,new_R,new_B,count+1,3)


def goright(map,posR,posB,count):
    #right
    new_R=list(posR)
    new_B=list(posB)

    for i in range(posB[1]+1,m) :
        if map[posB[0]][i] == 'O' :
            return 0
        if map[posB[0]][i] != '.':
            new_B[1]=i-1
            break

    for i in range(posR[1]+1,m) :
        if map[posR[0]][i] == 'O':
            return count
        elif map[posR[0]][i] != '.':
            if posR[0] == posB[0] :
                if i-1 == new_B[1] :
                    if posR[1] > posB[1] :
                        new_B[1] = i-2
                        new_R[1] = i-1
                    else :
                        new_B[1] = i-1
                        new_R[1] = i-2
            else :
                new_R[1]=i-1
            break

    return findMap(map,new_R,new_B,count+1,4)


import copy
def findMap(tempmap,posR,posB,count,pos):
    if count > 10:
        return 0
    if pos ==0 :
        map = copy.deepcopy(tempmap)
        a=goleft(map,list(posR),list(posB),count)
        map = copy.deepcopy(tempmap)
        b=goright(map,list(posR),list(posB),count)
        map = copy.deepcopy(tempmap)
        c=goup(map,list(posR),list(posB),count)
        map = copy.deepcopy(tempmap)
        d=godown(map,list(posR),list(posB),count)
    elif pos == 1:
        map = copy.deepcopy(tempmap)
        a=goleft(map,list(posR),list(posB),count)
        map = copy.deepcopy(tempmap)
        b=goright(map,list(posR),list(posB),count)
        c=0
        map = copy.deepcopy(tempmap)
        d=godown(map,list(posR),list(posB),count)
    elif pos == 2:
        map = copy.deepcopy(tempmap)
        a=goleft(map,list(posR),list(posB),count)
        map = copy.deepcopy(tempmap)
        b=goright(map,list(posR),list(posB),count)
        map = copy.deepcopy(tempmap)
        c=goup(map,list(posR),list(posB),count)
        d=0
    elif pos == 3:
        a=0
        map = copy.deepcopy(tempmap)
        b=goright(map,list(posR),list(posB),count)
        map = copy.deepcopy(tempmap)
        c=goup(map,list(posR),list(posB),count)
        map = copy.deepcopy(tempmap)
        d=godown(map,list(posR),list(posB),count)
    elif pos == 4:
        map = copy.deepcopy(tempmap)
        a=goleft(map,posR,posB,count)
        b=0
        map = copy.deepcopy(tempmap)
        c=goup(map,posR,posB,count)
        map = copy.deepcopy(tempmap)
        d=godown(map,posR,posB,count)

    temp = [a,b,c,d]
    if sum(temp)==0 :
        return 0

    return min(filter(lambda x : x>0, temp))


from sys import stdin
n, m = map(int, stdin.readline().split())
bigmap = []
for i in range(n):
    arr = list(stdin.readline())
    bigmap.append(arr)

posR = []
posB = []
for i in range(n) :
    for j in range(m) :
        if bigmap[i][j] == 'R' :
            posR.append(i)
            posR.append(j)
            bigmap[i][j]='.'
        elif bigmap[i][j] == 'B' :
            posB.append(i)
            posB.append(j)
            bigmap[i][j]='.'

a = findMap(bigmap,posR,posB,1,0)
if a==0 :
    print(-1)
else:
    print(a)