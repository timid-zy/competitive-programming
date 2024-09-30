class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count(x):
            ub = x + 1
            nums = 0
            while x <= n:
                if ub > n:
                    return nums + n - x + 1
                
                nums += ub - x
                ub *= 10
                x *= 10
                
            return nums
        
        curr = 1
        k -= 1
        while k > 0:
            N = count(curr)
            if N <= k:
                k -= N
                curr += 1
            else:
                k -= 1
                curr *= 10

        return curr
