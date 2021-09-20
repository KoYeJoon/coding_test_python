class Node :
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList :
    def __init__(self):
        self.head = None
        self.tail = None
        self.node_count = 0

    # 첫번째에 노드 추가
    def addFrontNode(self,data):
        self.node_count += 1
        temp = Node(data)
        if self.head == None :
            self.head = temp
            self.tail = temp
        else :
            temp.next = self.head
            self.head = temp

    # 마지막에 노드 추가
    def addLastNode(self,data):
        self.node_count += 1
        temp = Node(data)

        if self.head == None :
            self.head = temp
            self.tail = temp
        else :
            self.tail.next = temp
            self.tail = temp

    # node 삽입
    def insert(self,index,data):
        temp = Node(data)
        self.node_count += 1
        if self.head == None :
            if index == 0:
                self.head = temp
                self.tail = temp
            return

        if index == 0 :
            temp.next = self.head
            self.head = temp
            return

        if index==self.node_count-1 :
            self.tail.next = temp
            self.tail = temp
            return

        cur = self.head
        for i in range(0,index-1):
            if cur == None :
                self.node_count -= 1
                return
            cur = cur.next
        temp.next = cur.next
        cur.next = temp

    # 해당 Index의 node 삭제
    def deleteNode(self,index):
        cur = self.head
        prev = None
        for i in range(index):
            prev = cur
            cur = cur.next
        if cur==None :
            return
        self.node_count -= 1
        if prev==None :
            self.head = self.head.next
        else:
            prev.next = cur.next



    # linked list 출력
    def display(self):
        cur = self.head
        for i in range(self.node_count):
            print(cur.data,end=" ")
            cur = cur.next


single_linked_list = LinkedList()
single_linked_list.addLastNode(1)
single_linked_list.addLastNode(3)
single_linked_list.addFrontNode(2)
single_linked_list.display()