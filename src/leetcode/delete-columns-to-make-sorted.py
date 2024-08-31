class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for col in range(len(strs[0])):
            prev = strs[0][col]
            for row in range(1, len(strs)):
                if strs[row][col] < prev:
                    count += 1
                    break
                prev = strs[row][col]
        
        return count