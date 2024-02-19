class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def toDict(text):
            char_dict = {}
            for char in text:
                if char not in char_dict:
                   char_dict[char] = 1
                else:
                    char_dict[char] += 1
            return char_dict

        s1_dict = toDict(s1)
        s2_dict = toDict(s2[:len(s1)])
        valid = True
        for key in s1_dict:
            if key in s2_dict and s1_dict[key] == s2_dict[key]:
                continue
            else:
                valid = False
                break
        if valid:
            return True

        start = 1
        while start < len(s2) - len(s1) + 1:
            s2_dict[s2[start - 1]] -= 1
            if s2[start + len(s1) - 1] not in s2_dict:
                s2_dict[s2[start + len(s1) - 1]] = 1
            else:
                s2_dict[s2[start + len(s1) - 1]] += 1
            
            valid = True
            for key in s1_dict:
                if key in s2_dict and s1_dict[key] == s2_dict[key]:
                    continue
                else:
                    valid = False
                    break
            if valid:
                return True
            start += 1

        return False
