# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        s, c = set(allowed), 0
        for word in words:
            if len(set(word) - s) == 0: c += 1

        return c