# Problem: Count Vowel Strings in Ranges - https://leetcode.com/problems/count-vowel-strings-in-ranges/

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        def is_vowel(s):
            return len(s) > 0 and (s[0] in "aeiou") and (s[-1] in "aeiou")

        prefix = [0] * len(words)
        prefix[0] = 1 if is_vowel(words[0]) else 0
        for i in range(1, len(words)):
            prefix[i] = prefix[i-1]
            if is_vowel(words[i]):
                prefix[i] += 1
        
        res = []
        for l, r in queries:
            if l == 0:
                res.append(prefix[r])
            else:
                res.append(prefix[r] - prefix[l-1])
        
        return res