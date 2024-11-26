class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        heap = []
        for i in range(k):
            counter[nums[i]] += 1
            heappush(heap, -nums[i])
        
        max_window = [-heap[0]]
        l = 0
        for r in range(k, len(nums)):
            counter[nums[l]] -= 1
            heappush(heap, -nums[r])
            counter[nums[r]] += 1
            while heap and counter[-heap[0]] == 0:
                heappop(heap)
            
            max_window.append(-heap[0])
            l += 1
        
        return max_window