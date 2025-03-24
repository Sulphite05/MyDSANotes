from itertools import combinations

num = input()
n = len(num)


def dfs(st, i):
    print(st)
    if i == n: return int(st)
    get1 = dfs(st+num[i], i+1)
    get2 = int(st) + dfs(num[i], i+1)
    print(get1, get2- int(st))
    return get1 + get2

    # if i < n:
    #     ans = 0
    #     for j in range(i+1, n):
    #         get = dfs(int(num[i:j]), j)
    #         ans += val + get
    #     return ans
    # else:
    #     return 0


# print(dfs(num[0], 1))
print(list(combinations(range(1, n+1), 2)))