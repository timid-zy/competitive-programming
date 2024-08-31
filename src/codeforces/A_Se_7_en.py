def solve():
    input_ = input()
    n = int(input_)
    arr = list(map(int, list(input_)))
    
    if n % 7 == 0:
        print(n)
        return

    ans = None
    for i in range(len(arr) - 1, -1, -1):
        if ans is not None:
            break
        
        for j in range(0, 10):
            temp = arr[:]
            temp[i] = j
            num = "".join(map(str, temp))
            if int(num) % 7 == 0:
                ans = int(num)
                break
    
    if ans:
        print(ans)
        return
    
    print(n + (n % 7))

for _ in range(int(input())):
    solve()
