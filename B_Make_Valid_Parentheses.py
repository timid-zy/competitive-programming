s = input()
stack = []
_dict = {
    "(": ")"
}
pairs = 0
for i in range(len(s)):
    if s[i] == "(":
        stack.append(s[i])
    else:
        if len(stack) > 0 and stack[-1] == "(":
            stack.pop()
            pairs += 1
        else:
            stack.append(')')

print(pairs * 2)