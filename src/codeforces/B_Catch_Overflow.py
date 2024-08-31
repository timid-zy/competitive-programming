x = int(input())
val = 0
stack = [1]
flag = True

for _ in range(x):
    command = input()
    
    if command == "add":
        if stack[-1] >= pow(2, 32):
            flag = False
            print('OVERFLOW!!!')
            break
        else:
            val += stack[-1]
            if val >= pow(2, 32):
                flag = False
                print('OVERFLOW!!!')
                break

        
    elif command[:3] == "for":
        mult = int(command[4:])
        multiplier = min( pow(2, 32), stack[-1] * mult)
        stack.append(multiplier)
    
    elif command == "end":
        red = stack.pop()

if flag: print(val)