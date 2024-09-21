class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        stk = list(reversed(list(range(1, 10))))
        while stk:
            curr = stk.pop()
            if curr <= n:
                res.append(curr)
            
            for i in range(9, -1, -1):
                if curr * 10 + i <= n:
                    stk.append(curr * 10 + i)
        
        return res