for i in range(int(input())):
    s = input()
    if len(s) <= 1 or len(s) % 2 == 1:
        print('NO')
        continue

    ans = "YES" if s[:len(s) // 2] == s[len(s) // 2:] else "NO"
    print(ans)