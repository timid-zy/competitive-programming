from collections import defaultdict, deque

class Node:
    def __init__(self, val=0, prev=None, nxt=None):
        self.val = val
        self.nxt = None
        self.prev = None

class ListNode:
    def __init__(self):
        self.head = None
        self.tail = None
        self.nodes = defaultdict(deque)
    
    def insert(self, num, after):
        if len(self.nodes[after]) == 0:
            if self.head == None:
                self.head = Node(num)
                self.tail = self.head
                self.nodes[self.tail.val].append(self.tail)
            else:
                nw = Node(num, self.tail)
                self.tail.nxt = nw
                nw.prev = self.tail
                self.tail = nw
                self.nodes[nw.val].append(nw)
        
            return
        
        node = self.nodes[after][0]
        if node == self.tail:
            nw = Node(num, self.tail)
            self.tail.nxt = nw
            nw.prev = self.tail
            self.tail = nw
            self.nodes[nw.val].append(nw)
            return

        actual_nxt = node.nxt
        nw = Node(num, self.tail)
        node.nxt = nw
        actual_nxt.prev = nw
        nw.prev = node
        nw.nxt = actual_nxt
        self.nodes[nw.val].append(nw)
        
    def remove(self, num):
        if len(self.nodes[num]) == 0:
            return

        node = self.nodes[num].popleft()
        if node == self.head and node == self.tail:
            self.head = self.tail = None
        elif node == self.head:
            self.head = self.head.nxt
            self.head.prev = None
        elif node == self.tail:
            self.tail = self.tail.prev
            self.tail.nxt = None
        else:
            prev = node.prev
            nxt = node.nxt
            prev.nxt = nxt
            nxt.prev = prev
    
    def get_list(self):
        arr = []
        curr = self.head
        while curr:
            arr.append(curr.val)
            curr = curr.nxt
        
        return arr

lst = ListNode()
for _ in range(int(input())):
    I = input().split()
    if I[0] == "insert":
        lst.insert(int(I[1]), int(I[2]))
    else:
        lst.remove(int(I[1]))
        # print(lst.get_list())

res = lst.get_list()
print(*res)