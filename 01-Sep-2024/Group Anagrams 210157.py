# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = defaultdict(list)
        for word in strs:
            k = "".join(sorted(list(word)))
            dct[k].append(word)
        
        res = []
        for lst in dct.values():
            res.append(lst)
        
        return res