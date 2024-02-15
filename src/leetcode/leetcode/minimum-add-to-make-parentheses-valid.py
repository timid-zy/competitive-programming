class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        offset = 0
        moves = 0
        for i in range(len(s)):
            if s[i] == "(":
                if offset < 0:
                    moves += abs(offset)
                    offset = 0
                offset += 1
            elif s[i] == ")":
                offset -= 1
        
        return moves + abs(offset)