# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [arr[0]]
        for i in range(1, len(arr)):
            prefix.append(prefix[-1] ^ arr[i])
        
        res = []
        for x, y in queries:
            if x == 0:
                res.append(prefix[y])
            else:
                res.append(prefix[y] ^ prefix[x-1])
        
        return res