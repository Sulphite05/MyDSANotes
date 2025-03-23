n = int(input())
lst = list(map(int, input().split()))
moves = 0
for i in range(1, n):
    if lst[i-1] > lst[i]:
        a = lst[i-1]
        moves += a - lst[i]
        lst[i] = a
print(moves)
