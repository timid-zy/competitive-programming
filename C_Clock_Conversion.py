for _ in range(int(input())):
    s = input().strip()
    h = int(s[:2])
    m = s[3:]
    resH = s[:2]

    if h == 0:
        print(f"12:{m} AM")
    elif h < 12:
        print(f"{resH}:{m} AM")
    elif h == 12:
        print(f"{resH}:{m} PM")
    else:
        h -= 12
        if h < 10:
            resH = "0" + str(h)
        else:
            resH = str(h)
        print(f"{resH}:{m} PM")