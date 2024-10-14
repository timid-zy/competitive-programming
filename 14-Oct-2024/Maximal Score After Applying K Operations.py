class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = list(map(lambda x: -x, nums))
        heapify(heap)
        res = 0
        for _ in range(k):
            v = heappop(heap)
            res -= v
            heappush(heap, -math.ceil(-v / 3))
        
        return res