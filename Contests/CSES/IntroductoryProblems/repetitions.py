s = input()
st = 0
curr = s[0]
maxi = 0
for i, c in enumerate(s):
    if curr == c:
        maxi = max(maxi, i - st + 1)
    else:
        st = i
        curr = c
print(maxi)
