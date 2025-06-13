k = int(input())
for _ in range(k):
    n = int(input())
    print(2*n - 3)
    print(1, 1, n-1)
    for i in range(2, n-1):
        print(i, 1, n-i)
        print(i, n-i+1, n)
    print(n-1, 2, n)
    print(n, 1, n)




