# https://favtutor.com/blogs/avl-tree-python


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree(object):

    def insert(self, cur, key):
        if not cur:
            return Node(key)
        elif key < cur.value:
            cur.left = self.insert(cur.left, key)
        else:
            cur.right = self.insert(cur.right, key)

        cur.height = 1 + max(self.getHeight(cur.left),
                         self.getHeight(cur.right))

        bf = self.getBal(cur)
        # ll
        if bf > 1 and key < cur.left.value:
            return self.rRotate(cur)

        # rr
        if bf < -1 and key > cur.right.value:
            return self.lRotate(cur)

        # lr
        if bf > 1 and key > cur.left.value:
            cur.left = self.lRotate(cur.left)
            return self.rRotate(cur)

        # rl
        if bf < -1 and key < cur.right.value:
            cur.right = self.rRotate(cur.right)
            return self.lRotate(cur)

        return cur

    def lRotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.getHeight(z.left),
                      self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                      self.getHeight(y.right))

        return y

    def rRotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.getHeight(z.left),
                      self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                      self.getHeight(y.right))

        return y

    def getHeight(self, cur):
        if not cur:
            return 0

        return root.height

    def getBal(self, cur):
        if not cur:
            return 0

        return self.getHeight(cur.left) - self.getHeight(cur.right)

    def preOrder(self, cur):
        if not cur:
            return
        print("{0} ".format(cur.value), end="")
        self.preOrder(cur.left)
        self.preOrder(cur.right)

    def inOrder(self,cur):
        if not cur:
            return
        self.inOrder(cur.left)
        print("{0} ".format(cur.value), end="")
        self.inOrder(cur.right)

    def postOrder(self,cur):
        if not cur:
            return
        self.postOrder(cur.left)
        self.postOrder(cur.right)
        print("{0} ".format(cur.value), end="")

Tree = AVLTree()
root = None

root = Tree.insert(root, 1)
root = Tree.insert(root, 2)
root = Tree.insert(root, 3)
root = Tree.insert(root, 4)
root = Tree.insert(root, 5)
root = Tree.insert(root, 6)
'''
    2
   /  \
  1    4
      /  \
     3    5
           \
            6

'''
# Preorder Traversal
print("Preorder traversal of the",
      "constructed AVL tree is")
Tree.preOrder(root)
print()
Tree.inOrder(root)
print()
Tree.postOrder(root)