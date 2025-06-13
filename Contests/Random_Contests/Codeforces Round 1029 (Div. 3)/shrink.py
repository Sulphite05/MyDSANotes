k = int(input())
for _ in range(k):
    n = int(input())
    ans = [1] + list(range(3, n+1)) + [2]
    for i in ans:
        print(i, end=' ')
    print()




