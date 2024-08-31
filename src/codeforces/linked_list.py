class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def getArr(head):
    arr = []
    curr = head
    while curr:
        arr.append(curr.val)
        curr = curr.next
    return arr

node2 = Node(3)
node1 = Node(2, node2)
head = Node(1, node1)

print(getArr(head))