def kmp(needle, haystack):
    lps = [0] * len(needle)
    prev, i = 0, 1

    while i < len(needle):
        if needle[i] == needle[prev]:
            prev += 1
            lps[i] = prev
            i += 1
        elif prev == 0:
            lps[i] = 0
            i += 1
        else:
            prev = lps[prev - 1]

    ni = hi = 0
    while hi < len(haystack):
        if haystack[hi] == needle[ni]:
            ni += 1
            hi += 1
        elif ni == 0:
            hi += 1
        else:
            ni = lps[ni-1]