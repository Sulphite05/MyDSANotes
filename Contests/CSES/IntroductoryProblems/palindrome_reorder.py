from collections import Counter

s = input()
dct = Counter(s)
single = ''
final = []

for c in dct:
    if dct[c] & 1:
        if single:
            print("NO SOLUTION")
            break
        else:
            single = c * dct[c]
    else:
        final += [c] * (dct[c] >> 1)
else:
    final = final + [single] + final[::-1]
    print(''.join(final))
