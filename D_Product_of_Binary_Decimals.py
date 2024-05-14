check = [10, 11, 101, 111, 1111, 1101,1011, 1001, 10001, 11001, 10101, 10011, 11101,10111,11011, 11111]
set_ = set(check)

def checkEach(num):
    global check

    flag1 = True
    for i in range(len(check)):
        
        n = num
        st = i

        while n > 1:
            if n in check:
                return True
            
            flag = False
            for __ in range(len(check)):
        
                if n % check[st % len(check)] == 0:
                    n //= check[st % len(check)]
                    flag = True
                    break
                    
                st += 1
            
            if not flag: break

        if n > 1:
            flag1 = False
            break
        
    return True if flag1 else False


for _ in range(int(input())):
    n = int(input())

    if checkEach(n) or n == 1:
        print('YES')
    else:
        print('NO')