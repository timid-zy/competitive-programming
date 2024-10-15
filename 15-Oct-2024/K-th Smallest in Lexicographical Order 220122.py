# Problem: K-th Smallest in Lexicographical Order - https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def get_count(x):
            y = x + 1
            count = 0
            while x <= n:
                if x == n:
                    count += 1
                    break

                if y > n:
                    count += n - x + 1
                    break

                count += y - x
                y *= 10
                x *= 10
            
            return count

        curr = 1
        k -= 1
        while k > 0:
            count = get_count(curr)
            if k < count:
                curr *= 10
                k -= 1
            else:
                curr += 1
                k -= count
        
        return curr