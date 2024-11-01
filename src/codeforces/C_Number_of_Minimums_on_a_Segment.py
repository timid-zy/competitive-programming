class SegmentTree:

    def __init__(self, nums):
        self.nums = nums
        self.n = len(nums)
        self.tree = [[float('inf'), 0] for _ in range(self.n * 2)]
        
        self.build()
    
    def build(self):
        for i in range(self.n):
            self.tree[i + self.n] = [self.nums[i], 1]
        
        for i in range(self.n - 1, 0, -1):
            if self.tree[i*2][0] == self.tree[i*2 + 1][0]:
                self.tree[i] = [self.tree[i*2][0], self.tree[i*2][1] + self.tree[i*2 + 1][1]]
            elif self.tree[i*2][0] < self.tree[i*2 + 1][0]:
                self.tree[i] = self.tree[i*2][:]
            else:
                self.tree[i] = self.tree[i*2 + 1][:]
    
    def update(self, i, value):
        self.nums[i] = value
        i += self.n
        self.tree[i] = [value, 1]
        while i > 1:
            i //= 2
            if self.tree[i*2][0] == self.tree[i*2 + 1][0]:
                self.tree[i] = [self.tree[i*2][0], self.tree[i*2][1] + self.tree[i*2 + 1][1]]
            elif self.tree[i*2][0] < self.tree[i*2 + 1][0]:
                self.tree[i] = self.tree[i*2][:]
            else:
                self.tree[i] = self.tree[i*2 + 1][:]
    
    def range_sum(self, left, right):
        left += self.n
        right += self.n
        res, res_count = float('inf'), 0
        while left < right:
            if left & 1:
                if self.tree[left][0] < res:
                    res, res_count = self.tree[left]
                elif self.tree[left][0] == res:
                    res_count += self.tree[left][1]

                left += 1
            
            if right & 1:
                right -= 1
                if self.tree[right][0] < res:
                    res, res_count = self.tree[right]
                elif self.tree[right][0] == res:
                    res_count += self.tree[right][1]

            left //= 2
            right //= 2
        
        return res, res_count
            

def solve():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    seg = SegmentTree(arr)
    for _ in range(m):
        op, left, right = map(int, input().split())
        if op == 1:
            seg.update(left, right)
        else:
            mn, mnc = seg.range_sum(left, right)
            print(mn, mnc)


solve()