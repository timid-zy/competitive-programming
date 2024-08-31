class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {}
        start = 0
        len_of_curr = 0
        max_len = 0

        for end in range(len(s)):
            count[s[end]] = count.get(s[end], 0) + 1
            len_of_curr = max(count[s[end]], len_of_curr)

            if end - start + 1 - len_of_curr <= k:
                max_len = max(max_len, end - start + 1)
            else:
                count[s[start]] -= 1
                start += 1
        
        return max_len