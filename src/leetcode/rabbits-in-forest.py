class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answers.sort()
        i = 0
        rabbits = 0
       
        while i < len(answers):
            answer = answers[i]
            rabbits += answer + 1
            max_lim = answer + i + 1

            while i < len(answers) and i < max_lim and answer == answers[i]:
                i += 1
            
        return rabbits