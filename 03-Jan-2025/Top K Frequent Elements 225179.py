# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = [(-v, k) for k, v in Counter(nums).items()]
        heapify(heap)
        res = []
        for _ in range(k):
            __, v = heappop(heap)
            res.append(v)
        
        return res