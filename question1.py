def reconstructPermutation(s):
    perm = []
    low, high = 0, len(s)

    for c in s:
        if c == 'I':
            perm.append(low)
            low += 1
        elif c == 'D':
            perm.append(high)
            high -= 1

    perm.append(low)  

    return perm
s = "IDID"
print(reconstructPermutation(s))
