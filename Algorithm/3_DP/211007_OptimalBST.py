INF = int(1e9)
class Treenode():
    def __init__(self):
        self.key = 0
        self.left = None
        self.right = None


def OptimalBST(p):
    n= len(p)
    C = [[0 for i in range(n+1)] for j in range(n+2)]
    R = [[0 for i in range(n+1)] for j in range(n+2)]
    for i in range(1,n+1):
        C[i-1][i] = 0
        C[i][i] = p[i-1]
        R[i][i] = i

    for d in range(1,n):
        for i in range(1,n-d+1):
            j = i+d
            minval = INF

            for k in range(i,j+1):
                if C[i][k-1] + C[k+1][j] < minval :
                    minval = C[i][k-1] + C[k+1][j]
                    kmin = k

            R[i][j] = kmin
            # 수도코드랑 비교하였을 때 p와 R과 C의 범위 주의!
            sum_p = sum(p[i-1:j])
            C[i][j] = minval + sum_p

    return C,R

def tree(i,j):
    k=R[i][j]
    if k==0 :
        return
    else :
        p = Treenode(Keys[k])
        p.left = tree(i,k-1)
        p.right = tree(k+1,j)
        return p

Keys = ['A','B','C','D']
p = [0.1,0.2,0.4,0.3]
n = len(p)
C,R = OptimalBST(p)
print(C)
print(R)