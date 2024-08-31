class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        def rec(n, k):
            if n == 1:
                return 0 if k == 1 else 1
            
            mid = pow(2, n - 1)
            
            if k <= mid:
                return rec(n - 1, k)
            else:
                left = rec(n - 1, k - mid)
                return 0 if left == 1 else 1


        return rec(n, k) 