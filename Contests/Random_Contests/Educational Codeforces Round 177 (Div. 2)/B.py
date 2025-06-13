t = int(input())
for _ in range(t):
    n, k, x = list(map(int, input().strip().split()))
    lst = list(map(int, input().strip().split()))[::-1]
    summ = sum(lst)
    maxi = n*k
    full = x // summ
    tot = full * summ
    add = 0
    for num in lst:
        if tot < x:
            tot += num
            add += 1
        else: break
    res = maxi - full * n - add + 1
    print(max(0, res))
