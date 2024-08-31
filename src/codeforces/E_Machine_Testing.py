from math import ceil

def checkSeconds(hp, d, t):
    stack = [[d[0] * t, d[0]]]
    
    for i in range(1, len(d)):
        if len(stack) == 0:
            return False
        
        dmg = 0
        seconds = 0
        while True:
            
            if len(stack) == 0:
                return False
            curr = stack[-1]
            
            if curr[0] < hp[i] - dmg:
                stack.pop()
                dmg += curr[0]
                seconds += curr[0] // curr[-1]

            else:
                add = ceil((hp[i] - dmg) / curr[-1])
                seconds += add

                if curr[0] == hp[i] - dmg:
                    stack.pop()
                else:
                    curr[0] -= add * curr[-1]

                stack.append([d[i] * seconds, d[i]])
                break
        
    return True

for i in range(int(input())):
    input()
    hp = list(map(int, input().split()))
    dmg = list(map(int, input().split()))

    l, r = 0, 10 ** 9

    while l < r:
        mid = l + (r - l) // 2
        if checkSeconds(hp, dmg, mid):
            r = mid
        else:
            l = mid + 1
    
    print(l)