class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        curr = 0
        for i in range(k):
            if s[i] in vowels:
                curr += 1
        mx = curr
        for start in range(1, len(s) - k + 1):
            if s[start - 1] in vowels:
                curr -= 1
            if s[start + k - 1] in vowels:
                curr += 1
            mx = max(curr, mx)
        
        return mx
