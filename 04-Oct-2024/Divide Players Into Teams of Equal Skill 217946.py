# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        i, j = 1, len(skill) - 2
        skill.sort()
        t = skill[0] + skill[-1]
        chem = skill[0]*skill[-1]
        while i < j:
            if skill[i] + skill[j] != t:
                return -1
            
            chem += skill[i]*skill[j]
            i += 1
            j -= 1
        
        return chem