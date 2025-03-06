n = int(input())
ans = []
# x + 2y = A => eq for pile A
# 2x + y = B => eq for pile B
# x and y are total coins
# x = A - 2y
# 2(A - 2y) + y = B
# 2A - 4y + y = B
# 2A - 3y = B
# y = (2A - B) / 3
# x = A - 2((2A - B) / 3)
# x = (3A - 4A + 2B)/3
# x = (2B - A) / 3
# 3x + 3y = A + B
# x + y = (A + B) / 3

for _ in range(n):
    a, b = list(map(int, input().split()))
    if b > a: a, b = b, a # swapping
    if a > 2*b or (a+b) % 3:
        ans.append("NO")
    else:
        ans.append("YES")
for s in ans:
    print(s)
