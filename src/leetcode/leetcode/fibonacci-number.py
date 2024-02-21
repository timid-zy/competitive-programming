class Solution:
    def fib(self, n: int) -> int:
        def fibonacciAt(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            
            return fibonacciAt(n - 1) + fibonacciAt(n - 2)
        
        return fibonacciAt(n)