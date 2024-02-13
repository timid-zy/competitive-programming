class CacheItem:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.dict1 = {}

    def get(self, key: int) -> int:
        if key not in self.dict1:
            return -1
        
        curr_node = self.dict1[key]

        # delete from current position
        if curr_node == self.tail:
            return curr_node.val # if it is the last element
        if curr_node == self.head:
            self.head = self.head.next
        else:
            prev = curr_node.prev
            next = curr_node.next
            prev.next = next
            next.prev = prev

        
        # put at the end
        self.tail.next = curr_node
        curr_node.prev = self.tail
        self.tail = curr_node
        curr_node.next = None

        # print(f'GET {key}')
        # self.printCache()
        return curr_node.val
        
    def put(self, key: int, value: int) -> None:
        if key in self.dict1:
            curr_node = self.dict1[key]
            # delete from current position
            if curr_node == self.tail:
                curr_node.val = value
                return
            elif curr_node == self.head:
                self.head = self.head.next
            else:
                prev = curr_node.prev
                next = curr_node.next
                prev.next = next
                next.prev = prev

            # put at the end
            self.tail.next = curr_node
            curr_node.prev = self.tail
            self.tail = curr_node
            curr_node.next = None
            curr_node.val = value
            return 

        if self.capacity <= 0:
            deleted_key = self.head.key
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            if deleted_key in self.dict1:
                del self.dict1[deleted_key]
        
        new_node = CacheItem(key, value)
        if self.head is None or self.tail is None:
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
        self.tail = new_node
        self.dict1[key] = new_node
        # print(f'PUT {key}: {value}')
        # self.printCache()
        self.capacity -= 1
    
    def printCache(self):
        str1 = ""
        curr = self.head
        while curr:
            str1 += str(curr.val)
            curr = curr.next
        print(str1)

        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)