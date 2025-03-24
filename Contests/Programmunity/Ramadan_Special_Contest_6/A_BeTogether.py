n = int(input())
lst = list(map(int, input().strip().split()))
mini = min(lst)
maxi = max(lst)
res = float('inf')
if len(set(lst)) == 1:
    print(0)
else:
    for num in range(mini, maxi):
        curr = 0
        for val in lst:
            curr += (val-num)**2
        res = min(res, curr)
    print(res)
