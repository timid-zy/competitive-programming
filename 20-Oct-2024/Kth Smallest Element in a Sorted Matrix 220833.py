# Problem: Kth Smallest Element in a Sorted Matrix - https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for i in range(len(matrix)):
            heappush(heap, (matrix[i][0], 0, i))
        
        for _ in range(k-1):
            _, vidx, idx = heappop(heap)
            if vidx < len(matrix[idx]) - 1:
                heappush(heap, (matrix[idx][vidx+1], vidx + 1, idx))
            
        return heappop(heap)[0]
