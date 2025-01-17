class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        # st = curr = 0
        # for i in range(len(derived)-1):
        #     if derived[i] == 1:
        #         curr = 1 if curr == 0 else 0
        
        # return (derived[-1] == 0 and curr == st) or (derived[-1] == 1 and curr != st)

        r = 0
        for n in derived: r ^= n
        return r == 0