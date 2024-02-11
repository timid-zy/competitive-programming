class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.len = 0
        

    def get(self, index: int) -> int:
        self.print()
        if index > self.len - 1:
            return -1
        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.value if curr is not None else -1
        

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.len += 1
        

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if self.len == 0:
            self.addAtHead(val)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        self.len += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index == self.len:
            return self.addAtTail(val)
        if index > self.len - 1:
            return
        if index == 0:
            return self.addAtHead(val)
        
        prev = self.head
        for i in range(index - 1):
            prev = prev.next
        new_node = Node(val)
        nextN = prev.next
        prev.next = new_node
        new_node.next = nextN  
        self.len += 1

    def deleteAtIndex(self, index: int) -> None:
        if index > self.len - 1 or index < 0:
            return
        
        if index == 0:
            self.head = self.head.next
            return
        
        prev = self.head
        for i in range(index - 1):
            prev = prev.next
        
        deletedN = prev.next
        nextN = deletedN.next if deletedN is not None else None
        prev.next = nextN
        self.len -= 1
    
    def print(self):
        curr = self.head
        str1 = ""
        while curr:
            str1 += str(curr.value)
            curr = curr.next
        print(str1)
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)