# Problem: Design Circular Deque - https://leetcode.com/problems/design-circular-deque/

class ListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyCircularDeque:

    def __init__(self, k: int):
        self.head = self.tail = None
        self.k, self.len = k, 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        
        if self.len == 0:
            self.tail = self.head = ListNode(value)
        else:
            self.head.prev = ListNode(value, None, self.head)
            self.head = self.head.prev

        self.len += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        
        if self.len == 0:
            self.tail = self.head = ListNode(value)
        else:
            self.tail.next = ListNode(value, self.tail, None)
            self.tail = self.tail.next

        self.len += 1
        return True        

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        
        if self.len == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        
        self.len -= 1
        return True
        

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        
        if self.len == 1:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        
        self.len -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1

        return self.head.val

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.tail.val

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