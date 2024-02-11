class Solution:
    def numberOfWays(self, s: str) -> int:
        
        zero_count = 0
        one_count = 0
        n_01 = []
        n_10 = []

        for i in range(len(s)):
            if s[i] == "0":
                n_01.append(0)
                n_10.append(one_count)
                zero_count += 1
            elif s[i] == "1":
                n_01.append(zero_count)
                n_10.append(0)
                one_count += 1
        
        # compute the prefix
        for i in range(1, len(n_10)):
            n_10[i] = n_10[i - 1] + n_10[i]
            n_01[i] = n_01[i - 1] + n_01[i]
        
        count = 0
        for i in range(len(s)):
            if s[i] == "1":
                count += n_10[i]
            else: 
                count += n_01[i]
        
        return count