# Problem: Shortest Subarray with Sum at Least K - https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        Q = deque([(0, -1)])
        r_sum = 0
        min_len = float('inf')
        for i in range(len(nums)):
            r_sum += nums[i]
            while len(Q) > 0 and r_sum-Q[0][0] >= k:
                min_len = min(min_len, i-Q[0][1])
                Q.popleft()

            while len(Q) > 0 and Q[-1][0] >= r_sum:
                Q.pop()

            Q.append((r_sum, i))
        
        return min_len if min_len < len(nums) + 1 else -1