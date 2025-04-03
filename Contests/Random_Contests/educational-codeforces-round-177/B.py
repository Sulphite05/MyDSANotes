t = int(input())
for _ in range(t):
    n, k, x = list(map(int, input().strip().split()))
    lst = list(map(int, input().strip().split()))[::-1]
    maxi = n*k
    minus = 0
    summ = 0
    ans = 0
    ex = 0
    for num in lst:
        summ += num
        if summ >= x:
            ex = True
            break
        minus += 1

    if not ex:
        req = x / summ
        if req > k:
            print(0)
        else:
            req = int(req)
            minus = req * n
            curr = summ * req
            for num in lst:
                curr += num
                if curr >= x:
                    break
                minus += 1
            ans = maxi - minus
            print(ans)
    else:
        print(maxi - minus)

