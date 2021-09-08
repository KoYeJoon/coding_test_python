import sys
sys.setrecursionlimit(10**6)

class Node():
    def __init__(self,idx,x,y):
        self.idx = idx
        self.x = x
        self.y = y
        self.left = self.right = None

class BT():
    def __init__(self):
        self.root = None
        self.preorder_arr = []
        self.postorder_arr = []

    def insert(self,idx,x,y):
        if self.root is None :
            self.root = Node(idx,x,y)
            return
        self.current = self.root
        while True :
            if x < self.current.x :
                if self.current.left != None :
                    self.current = self.current.left
                else :
                    self.current.left = Node(idx,x,y)
                    break
            else :
                if self.current.right != None :
                    self.current = self.current.right
                else :
                    self.current.right = Node(idx,x,y)
                    break

    def preorder(self,node):
        if node != None :
            self.preorder_arr.append(node.idx)
            if node.left :
                self.preorder(node.left)
            if node.right :
                self.preorder(node.right)

    def postorder(self,node):
        if node != None :
            if node.left :
                self.postorder(node.left)
            if node.right :
                self.postorder(node.right)
            self.postorder_arr.append(node.idx)

def solution(nodeinfo):
    answer = []
    binary_tree = BT()
    newnodeinfo = []
    for idx, value in enumerate(nodeinfo) :
        newnodeinfo.append([idx+1,value[0], value[1]])
    newnodeinfo.sort(key=lambda x : x[2],reverse=True)
    for idx, tx,ty in newnodeinfo :
        binary_tree.insert(idx,tx, ty)

    binary_tree.preorder(binary_tree.root)
    binary_tree.postorder(binary_tree.root)
    answer.append(binary_tree.preorder_arr)
    answer.append(binary_tree.postorder_arr)

    return answer

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))
'''
class BT():
    def __init__(self):
        self.root = None
        self.preorder_arr = []
        self.postorder_arr = []

    def insert(self,idx,x,y):
        if self.root is None :
            self.root = Node(idx,x,y)
            return
        self.current = self.root
        while True :
            if y < self.current.y :
                if self.current.left != None :
                    self.current = self.current.left
                else :
                    self.current.left = Node(idx,x,y)
                    break
            elif y > self.current.y:
                if self.current.right != None :
                    self.current = self.current.right
                else :
                    self.current.right = Node(idx,x,y)
                    break
            else :
                if x < self.current.x :
                    if self.current.left != None :
                        self.current = self.current.left
                    else :
                        self.current.left = Node(idx,x,y)
                        break
                else :
                    if self.current.right != None :
                        self.current = self.current.right
                    else :
                        self.current.right = Node(idx,x,y)
                        break



    def preorder(self,node):
        if node != None :
            print(node.idx, node.x, node.y)
            self.preorder_arr.append(node.idx)
            if node.left :
                self.preorder(node.left)
            if node.right :
                self.preorder(node.right)

    def postorder(self,node):
        if node != None :
            if node.left :
                self.postorder(node.left)
            if node.right :
                self.postorder(node.right)
            self.postorder_arr.append(node.idx)'''