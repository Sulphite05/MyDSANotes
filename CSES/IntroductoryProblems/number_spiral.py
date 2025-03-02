times = int(input())
ans = []
for _ in range(times):
    m, n = list(map(int, input().split()))
    if m <= n:
        adj = 1 + n * (n - 1)
        if n & 1:
            adj += (n - m)
        else:
            adj -= (n - m)
        ans.append(adj)

    else:
        adj = 1 + m * (m - 1)
        if m & 1:
            adj -= (m - n)
        else:
            adj += (m - n)
        ans.append(adj)

for a in ans:
    print(a)
