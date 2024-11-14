class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def check_val(x):
            stores = n
            for i in range(len(quantities)):
                stores -= math.ceil(quantities[i] / x)
                if stores < 0:
                    return False
            
            return True
        
        quantities.sort(reverse=True)
        l, r = 1, max(quantities)
        while l < r:
            mid = (r + l) // 2
            if check_val(mid):
                r = mid
            else:
                l = mid + 1
        
        return l
