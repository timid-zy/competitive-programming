class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()

        start = 0
        end = len(skill) - 1
        chemistry = 0
        target = skill[0] + skill[-1]

        while start < end:
            curr_sum = skill[start] + skill[end]
            if curr_sum == target:
                chemistry += (skill[start] * skill[end])
                start += 1
                end -= 1
            else:
                return -1

        return chemistry