class Solution:
    def maxScore(self, s: str) -> int:
        # 4:06 - 
        prefix_sum = [0] * len(s)
        postfix_sum = [0] * len(s)
        prefix_sum[0] = 1 if s[0] == "0" else 0
        postfix_sum[-1] = 1 if s[-1] == "1" else 0

        for i in range(1, len(s)):
            if s[i] == "0":
                prefix_sum[i] = prefix_sum[i - 1] + 1
            else: 
                prefix_sum[i] = prefix_sum[i - 1]

            if s[len(s) - i - 1] == "1":
                postfix_sum[len(s) - i - 1] = postfix_sum[len(s) - i] + 1
            else:
                postfix_sum[len(s) - i - 1] = postfix_sum[len(s) - i]

        max1 = prefix_sum[1] + postfix_sum[1]
        if len(s) == 2:
            if s[0] == s[1]:
                return 1
            elif s[0] == "0":
                return 2
            else:
                return 0

        for i in range(2, len(s) - 1):
            max1 = max(max1, prefix_sum[i] + postfix_sum[i])
        
        return max1
