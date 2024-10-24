# Problem: Repeated String Match - https://leetcode.com/problems/repeated-string-match/description/

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        mn = math.ceil(len(b) / len(a))
        if self.check_kmp(a*mn, b):
            return mn
        elif self.check_kmp(a*(mn+1), b):
            return mn + 1
        
        return -1

    # rabin-karp
    def check_rk(self, H, N):
        aks = [1] * len(N)
        MOD = 10 ** 9 + 7
        for i in range(len(N) - 2, -1, -1):
            aks[i] = aks[i+1] * 27
        
        curr = target = 0
        for i in range(len(N) - 1, -1, -1):
            target = (target + (ord(N[i])- 96) * aks[i]) % MOD
            curr = (curr + (ord(H[i])- 96) * aks[i]) % MOD
        
        if curr == target:
            return True
        
        for i in range(1, len(H) - len(N) + 1):
            ni = i + len(N) - 1
            curr = (curr - (ord(H[i-1])-96) * aks[0]) % MOD
            curr = (curr * 27) % MOD
            curr = (curr + (ord(H[ni])-96)) % MOD

            if curr == target:
                return True
        
        return False
    
    # kmp
    def check_kmp(self, H, N):
        if len(N) > len(H):
            return False

        lps = [0] * len(N)
        l, r = 0, 1
        while r < len(N):
            if N[l] == N[r]:
                l += 1
                lps[r] = l
                r += 1
            elif l == 0:
                r += 1
            else:
                l = lps[l-1]
        
        ni = hi = 0
        while ni < len(N) and hi < len(H):
            if N[ni] == H[hi]:
                ni += 1; hi += 1
            elif ni == 0:
                hi += 1
            else:
                ni = lps[ni-1]
        
        return ni == len(N)