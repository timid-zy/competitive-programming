import math
input()
walls = list(map(int, input().split()))
sorted_walls = sorted(walls)

def checkAtk(d):
    min1, min2 = sorted_walls[0], sorted_walls[1]
    if math.ceil(min1 / 2) + math.ceil(min2 / 2) <= d: return True

    for i in range(1, len(walls)):
        x = max(walls[i], walls[i - 1])
        y = min(walls[i], walls[i - 1])

        if i != len(walls) - 1 and math.ceil((walls[i - 1] + walls[i + 1]) / 2) <= d:
            return True
        elif max(math.ceil(x / 2), math.ceil((x + y) / 3)) <= d:
            return True

    
    return False

l, r = 1, pow(10, 12)
while l < r:
    mid = l + (r - l) // 2
    if checkAtk(mid):
        r = mid
    else:
        l = mid + 1

print(l)