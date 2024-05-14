for i in range(int(input())):
    input()
    s = input()

    count = 0
    i = 3
    while i <= len(s):
        if s[i - 3: i] == "map" or s[i - 3: i] == "pie":
            count += 1
            i += 3
        else:
            i += 1
    
    print(count)