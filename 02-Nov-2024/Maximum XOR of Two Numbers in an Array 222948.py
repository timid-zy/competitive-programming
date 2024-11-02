# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        class TrieNode():
            def __init__(self):
                self.children = [None, None]
                self.is_end = False
        
        def insert(root, n):
            curr = root
            for i in range(32, -1, -1):
                c = (n & (1 << i)) >> i
                if curr.children[c] == None:
                    curr.children[c] = TrieNode()
                
                curr = curr.children[c]
            
            curr.is_end = True

        def get_best(root, n):
            n = n | (1 << 33)
            n = ~n
            res = 0
            curr = root
            for i in range(32, -1, -1):
                c = (n & (1 << i)) >> i
                op = 1 if c == 0 else 0
                if curr.children[c] == None:
                    curr = curr.children[op]
                    if op == 1:
                        res |= (1 << i)
                else:
                    curr = curr.children[c]
                    if c == 1:
                        res |= (1 << i)
            
            return res
        
        root = TrieNode()
        for n in nums:
            insert(root, n)
        
        mx = float('-inf')
        for n in nums:
            mx = max(mx, n^get_best(root, n))

        return mx