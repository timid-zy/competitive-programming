for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    a = [True] * (n)

    c = 0
    e = 1
    ans = []
    
    for i in range(len(arr)):
        if e - c == arr[i]:
            ans.append(str(c))
            a[c] = False
            c += 1
            while c < len(a) and a[c] == False:
                c += 1
            
            if c == e:
                e += 1
            while e < len(a) and a[e] == False:
                e += 1
        
        else:
            target = c - arr[i]
            a[target] = False
            ans.append(str(target))

            while e < len(a) and a[e] == False:
                e += 1
    
    ans = " ".join(ans)
    print(ans)