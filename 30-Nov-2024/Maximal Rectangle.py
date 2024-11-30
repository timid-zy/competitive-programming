class Solution:
    def largestRectangle(self, row):
        stk = []
        res = 0
        for i, h in enumerate(row):
            c = 0
            while stk and stk[-1][0] >= h:
                oh, oc = stk.pop()
                c += oc
                res = max(res, c * oh)
            
            stk.append((h, c+1))
        
        c = 0
        while stk:
            oh, oc = stk.pop()
            c += oc
            res = max(res, c * oh)
        
        return res


    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        dp = list(map(int, matrix[0][:]))
        res = self.largestRectangle(dp)
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    dp[j] += 1
                else:
                    dp[j] = 0
            
            res = max(res, self.largestRectangle(dp))

        return res
        