n = int(input())
s = input()

st = 1
i = 0
res = ""
while i < len(s):
    res += s[i]
    i += st
    st += 1

print(res)