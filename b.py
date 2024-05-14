def get_binary(num):
    if num == 0:
        return [0]

    d, r = divmod(num, 2)
    num = d
    b = [r]
    while num >= 1:
        d, r = divmod(num, 2)
        b.append(r)
        num = d
    
    return b[::-1]

print(get_binary(16))