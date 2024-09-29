class ListNode:
    def __init__(self, freq, prev=None, next=None):
        self.freq = freq
        self.prev = prev
        self.next = next
        self.keys = set()

class AllOne:

    def __init__(self):
        self.head = self.tail = None
        self.map = {}

    def delete_node(self, node):
        if node == self.head and node == self.tail:
            self.head = self.tail = None
        elif node == self.head:
            self.head = self.head.next
            self.head.prev = None
        elif node == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            prev, next = node.prev, node.next
            prev.next = next
            next.prev = prev

        
    def inc(self, key: str) -> None:
        if key not in self.map:
            if self.head is None:
                self.head = self.tail = ListNode(1)
            elif self.head.freq > 1:
                self.head.prev = ListNode(1, None, self.head)
                self.head = self.head.prev
            
            self.head.keys.add(key)
            self.map[key] = self.head
            return
        
        node = self.map[key]
        orf = node.freq
        if node.next and node.next.freq == orf + 1:
            node.keys.remove(key)
            node.next.keys.add(key)
            self.map[key] = node.next
        else:
            if node == self.tail:
                node.next = ListNode(orf + 1, node, None)
                self.tail = node.next
            else:
                nxt = node.next
                newN = ListNode(orf + 1, node, nxt)
                if node.prev:
                    node.prev.next = newN

                node.next = newN
                nxt.prev = newN
            
            node.keys.remove(key)
            node.next.keys.add(key)
            self.map[key] = node.next    
    
        if len(node.keys) == 0:
            self.delete_node(node)
        

    def dec(self, key: str) -> None:
        node = self.map[key]
        orf = node.freq
        if orf == 1:
            node.keys.remove(key)
            del self.map[key]
        elif node.prev and node.prev.freq == orf - 1:
            node.keys.remove(key)
            node.prev.keys.add(key)
            self.map[key] = node.prev
        else:
            if node == self.head:
                node.prev = ListNode(orf - 1, None, node)
                self.head = node.prev
            else:
                prev = node.prev
                prev.next = ListNode(orf-1, prev, node)
                node.prev = prev.next
            
            node.keys.remove(key)
            node.prev.keys.add(key)
            self.map[key] = node.prev

        if len(node.keys) == 0:
            self.delete_node(node)      

    def getMaxKey(self) -> str:
        if not self.tail or len(self.tail.keys) == 0:
            return ""

        v = self.tail.keys.pop()
        self.tail.keys.add(v)
        return v

    def getMinKey(self) -> str:
        if not self.head or len(self.head.keys) == 0:
            return ""

        v = self.head.keys.pop()
        self.head.keys.add(v)
        return v
    
    def __str__(self):
        curr = self.head
        if not curr: return ""
        res = f"HEAD: {self.head.freq}\nTAIL: {self.tail.freq}\n"
        while curr != None:
            res += f"<-{curr.freq} {curr.keys}->"
            curr = curr.next

        return res        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()