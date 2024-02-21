class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)
        def decode(s):
            if len(s) == 0 or s[0] == "]":
                return ""
            
            if not s[0].isnumeric():
                str1 = decode(s[1:])
                return s[0] + str1
            else:
                num = ""
                num_idx = 0
                while s[num_idx].isnumeric():
                    num += s[num_idx]
                    num_idx += 1
                str1 = decode(s[num_idx + 1:])
                offset = 0
                idx = 0
                for i in range(num_idx + 1, len(s)):
                    if s[i] == "[": offset += 1
                    elif s[i] == "]":
                        if offset == 0:
                            idx = i
                            break
                        offset -= 1
                # print(num_idx)
                return (int(num) * str1) + decode(s[idx + 1:])
        
        return decode(s)
        