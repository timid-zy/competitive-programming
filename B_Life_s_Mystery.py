s = input()

stack = []
for i in range(len(s)):
    if len(stack) == 0:
        stack.append(s[i])
        continue

    if stack[-1] == s[i]:
        stack.pop()
        continue

    stack.append(s[i])

print("".join(stack))