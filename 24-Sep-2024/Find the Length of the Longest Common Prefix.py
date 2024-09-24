class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        class TrieNode():
            def __init__(self):
                self.children = {}
                self.is_end = False
        

        def get_digits(num):
            res = []
            while num > 0:
                res.append(num%10)
                num //= 10
            
            return res[::-1]
        
        def add(num, root):
            parent = root
            for c in get_digits(num):
                if c not in parent.children:
                    parent.children[c] = TrieNode()
                
                parent = parent.children[c]
            
            parent.is_end = True
        
        def find_prefix_len(num, root):
            parent = root
            curr = 0
            for c in get_digits(num):
                if c not in parent.children:
                    return curr
                
                parent = parent.children[c]
                curr += 1
            
            return curr
        
        root = TrieNode()
        for w in arr1:
            add(w, root)
        
        res = 0
        for w in arr2:
            res = max(
                res,
                find_prefix_len(w, root)
            )
        
        return res
    