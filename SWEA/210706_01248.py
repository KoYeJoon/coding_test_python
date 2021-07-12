T = int(input())

class Node :
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def find_common_parent(root,v1,v2):
    if root in (v1,v2,None):
        if root != None :
            print(root.val)
        return root
    left_child = find_common_parent(root.left,v1,v2)
    right_child = find_common_parent(root.right,v1,v2)
    print(root.val, left_child, right_child)
    return root if (left_child and right_child) else left_child or right_child

def count_child(root):
    if root :
        left = count_child(root.left)
        right = count_child(root.right)
        return 1 + left + right

    return 0

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    v,e,v1,v2 = map(int,input().split())
    tree = [Node(x) for x in range(v+1)]
    list_n = list(map(int,input().split()))

    for i in range(0,2*e,2):
        parent,child = tree[list_n[i]],tree[list_n[i+1]]
        if not parent.left :
            parent.left = child
        else :
            parent.right = child

    print(f'#{test_case}',end=' ')
    common_parent = find_common_parent(tree[1],tree[v1],tree[v2])
    cnt = count_child(common_parent)
    print(f'{common_parent.val} {cnt}')