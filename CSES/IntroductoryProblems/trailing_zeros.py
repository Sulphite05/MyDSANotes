n = int(input())
fives, ans = 5, 0
while n // fives:
    ans += n//fives
    fives *= 5
print(ans)
