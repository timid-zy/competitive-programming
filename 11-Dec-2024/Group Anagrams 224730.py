# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for s in strs:
            mp["".join(sorted(s))].append(s)
        
        res = []
        for v in mp.values():
            res.append(v)
        
        return res