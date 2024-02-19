class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        seen_chars = {}
        longest = 0

        while start < len(s) and end < len(s):
            if s[end] in seen_chars and seen_chars[s[end]] >= start:
                longest = max(longest, end - start)
                start = seen_chars[s[end]] + 1
            seen_chars[s[end]] = end
            end += 1
        
        longest = max(longest, end - start)
        return longest
                