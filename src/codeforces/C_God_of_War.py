def min_pow(arr):
    curr = beaten = 0
    for n in arr:
        if n >= curr + beaten:
            curr = (n + 1) - beaten
        
        beaten += 1
    
    return curr

def check_pow(x, caves):
    for cave, _ in caves:
        for c in cave:
            if c < x:
                x += 1
            else:
                return False
    
    return True

def solve():
    N = int(input())
    caves = []
    for _ in range(N):
        arr = list(map(int, input().split()))[1:]
        caves.append((arr, min_pow(arr)))
    
    caves.sort(key=lambda x: x[1])
    l, r = 0, 10 ** 9 + 2
    while l < r:
        mid = (r + l) // 2
        if check_pow(mid, caves):
            r = mid
        else:
            l = mid + 1
        
    return l

for _ in range(int(input())):
    print(solve())