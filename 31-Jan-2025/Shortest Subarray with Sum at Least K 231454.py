# Problem: Shortest Subarray with Sum at Least K - https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        queue = deque([(0, -1)])
        r_sum = 0
        res = float('inf')
        for i in range(len(nums)):
            r_sum += nums[i]
            while len(queue) > 0 and r_sum - queue[0][0] >= k:
                res = min(res, i-queue[0][1])
                queue.popleft()

            while len(queue) > 0 and queue[-1][0] >= r_sum:
                queue.pop()

            queue.append((r_sum, i))
        
        return res if res <= len(nums) else -1