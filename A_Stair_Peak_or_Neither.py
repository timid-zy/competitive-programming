for i in range(int(input())):
    x, y, z = list(map(int, input().split()))
    if x < y and y < z:
        print('STAIR')
    elif x < y and y > z:
        print('PEAK')
    else:
        print('NONE')