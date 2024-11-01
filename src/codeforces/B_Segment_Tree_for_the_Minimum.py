class MinSegmentTree:
    def __init__(self, nums):
        self.nums = nums
        self.n = len(nums)
        self.tree = [float('inf')] * (2 * self.n)

        self.build()
    
    def build(self):
        for i in range(self.n):
            self.tree[i+self.n] = self.nums[i]
        
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = min(self.tree[2*i], self.tree[2*i + 1])
        
    def update(self, index, val):
        self.nums[index] = val
        self.tree[index + self.n] = val
        i = (index + self.n) // 2
        while i >= 1:
            self.tree[i] = min(self.tree[2*i], self.tree[2*i + 1])
            i //= 2

    def range_min(self, left, right):
        left += self.n
        right += self.n + 1
        res = float('inf')
        while left < right:
            if left % 2 == 1:
                res = min(res, self.tree[left])
                left += 1
            
            if right % 2 == 1:
                right -= 1
                res = min(res, self.tree[right])
            
            left //= 2
            right //= 2
        
        return res

def solve():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    seg = MinSegmentTree(A)

    for _ in range(m):
        t, l, r = map(int, input().split())
        if t == 1:
            seg.update(l, r)
        else:
            print(seg.range_min(l, r-1))

solve()