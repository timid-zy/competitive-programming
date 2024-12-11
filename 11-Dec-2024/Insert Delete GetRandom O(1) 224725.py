# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/

class RandomizedSet:

    def __init__(self):
        self.items = []
        self.hmp = {}

    def insert(self, val: int) -> bool:
        if val in self.hmp:
            return False
        
        self.items.append(val)
        self.hmp[val] = len(self.items) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hmp:
            return False
        
        lst = self.items[-1]
        self.hmp[lst] = self.hmp[val]
        self.items[-1], self.items[self.hmp[val]] = self.items[self.hmp[val]], self.items[-1]
        self.items.pop()
        del self.hmp[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.items)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()