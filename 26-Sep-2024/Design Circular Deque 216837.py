# Problem: Design Circular Deque - https://leetcode.com/problems/design-circular-deque/

class ListNode:
    def __init__(self, val=0, prev=None, nxt=None):
        self.val = val
        self.prev = prev
        self.next = nxt
    
    def __str__(self):
        return str(self.val)

class MyCircularDeque:

    def __init__(self, k: int):
        self.head = None
        self.tail = None
        self.k = k
        self.len = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        self.len += 1
        if self.len == 1:
            self.head = self.tail = ListNode(value)
            return True
        
        newNode = ListNode(value, None, self.head)
        self.head.prev = newNode
        self.head = self.head.prev
        return True


    def insertLast(self, value: int) -> bool:
        if self.len == self.k:
            return False

        self.len += 1
        if self.len == 1:
            self.head = self.tail = ListNode(value)
            return True
        
        newNode = ListNode(value, self.tail, None)
        self.tail.next = newNode
        self.tail = self.tail.next
        return True
        

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        
        self.len -= 1
        if self.len == 0:
            self.tail = self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None
        
        return True
        

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        self.len -= 1
        if self.isEmpty():
            self.tail = self.head = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        return True
        
    def getFront(self) -> int:
        return self.head.val if not self.isEmpty() else -1
        
    def getRear(self) -> int:
        return self.tail.val if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return self.len == 0
        
    def isFull(self) -> bool:
        return self.len == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()