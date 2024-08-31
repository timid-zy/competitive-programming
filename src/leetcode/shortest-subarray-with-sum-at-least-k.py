class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        queue = deque()
        queue.append((0, -1))
        r_sum = 0
        min_len = len(nums) + 1

        for i in range(len(nums)):
            r_sum += nums[i]
            
            while len(queue) > 0 and r_sum - queue[0][0] >= k:
                min_len = min(min_len, i - queue[0][1])
                queue.popleft()
            
            while len(queue) > 0 and queue[-1][0] > r_sum:
                queue.pop()

            queue.append((r_sum, i))
        
        return min_len if min_len < len(nums) + 1 else -1