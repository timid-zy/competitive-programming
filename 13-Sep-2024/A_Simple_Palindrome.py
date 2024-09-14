for _ in range(int(input())):
    N = int(input())
    res = [0, 0, 0, 0, 0]
    curr = N
    i = 0
    while curr > 0:
        res[i] += 1
        i = (i + 1) % 5
        curr -= 1
    
    vowels = ["a", "e", "i", "o", "u"]
    ans = ""
    for i in range(5):
        ans += vowels[i] * res[i]
    
    print(ans)