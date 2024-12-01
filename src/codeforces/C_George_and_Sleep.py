st, sm = map(int, input().split(":"))
et, em = map(int, input().split(":"))

rest = (st - et) % 24
resm = (sm - em) % 60
if em > sm:
    rest = (rest - 1) % 24

h = str(rest)
if len(h) == 1: h = "0" + h
m = str(resm)
if len(m) == 1: m = "0" + m

print(h+":"+m)