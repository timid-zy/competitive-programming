# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r1, r2, r3 = set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")
        res = []
        for word in words:
            r = set()
            for c in word.lower():
                if c in r1: r.add("1")
                if c in r2: r.add("2")
                if c in r3: r.add("3")

            if len(r) == 1:
                res.append(word) 
        
        return res
