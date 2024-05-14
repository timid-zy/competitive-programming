h = int(input())

count = 0
for x in range(4, h + 1):

    d = 2
    divs = set()
    while d * d <= x:
        if x % d != 0:
            d += 1
            continue

        x //= d
        divs.add(d)
    
    if x > 1:
        divs.add(x)
    
    if len(divs) == 2:
        count += 1
    
print(count)