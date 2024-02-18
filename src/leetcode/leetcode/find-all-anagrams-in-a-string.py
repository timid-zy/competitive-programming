class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def toDict(text):
            dict1 = {}
            for i in text:
                if i not in dict1:
                    dict1[i] = 1
                else:
                    dict1[i] += 1
            return dict1
        
        pD = toDict(p)
        sD = toDict(s[:len(p)])
        anagrams = [0]
        for letter in pD:
            if letter not in sD or sD[letter] == 0 or sD[letter] != pD[letter]:
                anagrams.pop()
                break

        for i in range(1, len(s) - len(p) + 1):
            sD[s[i - 1]] -= 1
            if s[i + len(p) - 1] not in sD:
                sD[s[i + len(p) - 1]] = 1
            else:
                sD[s[i + len(p) - 1]] += 1
            
            anagrams.append(i)
            for letter in pD:
                if letter not in sD or sD[letter] == 0 or sD[letter] != pD[letter]:
                    anagrams.pop()
                    break

        return anagrams