n = int(input())

while n > 1:
    print(n, end=' ')
    if n & 1:
        n = n * 3 + 1
    else:
        n = n >> 1
print(1, end=' ')
