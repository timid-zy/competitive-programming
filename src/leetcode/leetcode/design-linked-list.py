class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.len = 0

    def get(self, index: int) -> int:
        self.print()
        curr = self.head
        i = 0
        while i < index and curr:
            curr = curr.next
            i += 1
        return curr.val if curr is not None else -1
        
    def addAtHead(self, val: int) -> None:
        return self.addAtIndex(0, val)
        
    def addAtTail(self, val: int) -> None:
        list_len = 0
        curr = self.head
        while curr:
            curr = curr.next
            list_len += 1
        return self.addAtIndex(list_len, val )
        
    def addAtIndex(self, index: int, val: int) -> None:
        dummy = Node(0, self.head)
        prev = dummy
        i = 0
        while i < index and prev:
            prev = prev.next
            i += 1
        if prev is None:
            return
        new_node = Node(val)
        new_node.next = prev.next
        prev.next = new_node
        self.head = dummy.next
        
    def deleteAtIndex(self, index: int) -> None:
        dummy = Node(0, self.head)
        prev = dummy
        i = 0
        while i < index and prev:
            prev = prev.next
            i += 1
        if prev is None:
            return
        prev.next = prev.next.next if prev.next else None
        self.head = dummy.next

    def print(self):
        s = ""
        curr = self.head
        while curr:
            s += str(curr.val)
            curr = curr.next
        print(s)


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)