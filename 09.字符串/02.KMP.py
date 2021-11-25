def get_next(p):
    next = [0]
    now = 0
    x = 1
    while x < len(p):
        if p[now] == p[x]:
            now += 1
            x += 1
            next.append(now)
        elif p[now] != p[x] and now != 0:
            now = next[now-1]
        elif p[now] != p[x] and now == 0:
            next.append(0)
            x += 1
    return next

def KMP(s,p):
    tar,pos = 0,0
    next = get_next(p)
    while tar < len(s) and pos < len(p):
        if s[tar] == p[pos]:
            tar += 1
            pos += 1
        elif s[tar] != p[pos] and pos != 0:
            pos = next[pos-1]
        elif s[tar] != p[pos] and pos == 0:
            tar += 1
    if pos == len(p):
        return tar-pos
    else:
        return -1

if __name__ == "__main__":
    result = KMP("abcab","cab")
    print(result)