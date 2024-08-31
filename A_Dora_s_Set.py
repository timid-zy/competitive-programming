for _ in range(int(input())):
    l, r = map(int, input().split())

    if l % 2 == 0: l += 1
    count = 0
    curr = l + 2
    while curr <= r:
        count += 1
        curr += 4
    
    print(count)