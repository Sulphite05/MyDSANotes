n = int(input())
ans = []
for _ in range(n):
    a, b = list(map(int, input().split()))
    maxi, mini = max(a, b), min(a, b)
    diff = (maxi-mini)
    maxi -= diff