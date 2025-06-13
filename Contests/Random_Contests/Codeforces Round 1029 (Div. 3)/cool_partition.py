k = int(input())
for _ in range(k):
    n = int(input())
    lst = input().split()
    curr = 1
    s = {lst[0]}
    c = set()
    nxt = set()
    for i in range(1, n):
        if lst[i] in s:
            c.add(lst[i])
        else:
            nxt.add(lst[i])

        if len(s) == len(c):
            c = set()
            s = s.union(nxt)
            curr += 1
    print(curr)









