def BF(s,p):
    n1 = len(s)
    n2 = len(p)
    i,j = 0,0
    while i < n1 and j < n2:
        if s[i] == p[j]:
            i += 1
            j += 1
        else:
            i = i - j + 1
            j = 0
    if j == n2:
        return i-j
    else:
        return -1

if __name__ == "__main__":
    result = BF("abcab","cab")
    print(result)