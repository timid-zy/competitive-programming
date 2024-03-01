class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0 if k == 1 else 1
        midPoint = pow(2, n-1 )
        if k <= midPoint:
            return self.kthGrammar(n-1, k)
        else:
            itemOnLeftSide = self.kthGrammar(n-1, k-midPoint)
            return 0 if itemOnLeftSide == 1 else 1