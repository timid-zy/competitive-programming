for _ in range(int(input())):
    input()
    arr = list(map(int, input().split()))
    odds = evens = 0
    for n in arr:
        if n % 2 == 0:
            evens += 1
        else:
            odds += 1
    
    ans = "Yes" if evens == odds else "No"
    print(ans)
    