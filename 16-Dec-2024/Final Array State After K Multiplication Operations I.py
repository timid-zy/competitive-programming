class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = list(zip(nums, range(len(nums))))
        heapify(heap)
        for _ in range(k):
            n, i = heappop(heap)
            heappush(heap, (n*multiplier, i))
        
        for n, i in heap:
            nums[i] = n
        
        return nums