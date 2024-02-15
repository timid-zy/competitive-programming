class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        pal_len = 0
        hasOneOdd = False
        for i in range(len(s)):
            if s[i] not in count:
                continue
            
            if count[s[i]] % 2 == 0:
                pal_len += count[s[i]]
            else:
                pal_len += (count[s[i]] // 2) * 2
                if not hasOneOdd:
                    pal_len += 1
                    hasOneOdd = True
            count.pop(s[i])
        
        return pal_len
            