class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.head = None
        self.tail = None
        self.max = k
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        new_node = Node(value)
        
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return True
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.size += 1
        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        if self.size == 1:
            self.tail = None
            self.head = None
            self.size -= 1
            return True
        
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        
        self.size -= 1
        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.val       

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        print(self.tail)
        return self.tail.val
        

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()