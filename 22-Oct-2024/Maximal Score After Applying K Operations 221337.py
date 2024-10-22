# Problem: Maximal Score After Applying K Operations - https://leetcode.com/problems/maximal-score-after-applying-k-operations

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        res = 0
        arr = list(map(lambda x: -x, nums))
        heapify(arr)
        for _ in range(k):
            v = -heappop(arr)
            res += v
            heappush(arr, -math.ceil(v/3))
        
        return res