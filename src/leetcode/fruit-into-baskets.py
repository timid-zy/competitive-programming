class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        start = 0
        last = {}
        mx = 0
        for i in range(len(fruits)):
            if len(last) != 2:
                last[fruits[i]] = i
                continue
            
            if fruits[i] in last.keys():
                last[fruits[i]] = i
            else:
                mx = max(mx, i - start)
                start = min(last.values()) + 1
                second = max(last.values())
                last = {fruits[start]: second, fruits[i]: i}
        
        return max(mx, len(fruits) - start)
