from collections import Counter
def checkPalindrome(s):
    return s == s[::-1]

for i in range(int(input())):
    s = input()
    counter = Counter(s)
    if len(counter) == 1:
        print(-1)
        continue
    
    if checkPalindrome(s):
        print(len(s) - 1)
    
    else:
        print(len(s))