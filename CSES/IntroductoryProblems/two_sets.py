n = int(input())

summ = (n * (n + 1)) >> 1
if summ & 1:
    print("NO")

else:
    print("YES")
    set1 = []
    set2 = []
    i, j = 1, n
    if n & 1:
        set2.append(str(n))
        j = n - 1
    one = True
    while i < j:
        if one:
            set1.append(str(i))
            set1.append(str(j))
        else:
            set2.append(str(i))
            set2.append(str(j))
        i += 1
        j -= 1
        one = not one

    print(len(set1))
    print(' '.join(set1))
    print(len(set2))
    print(' '.join(set2))
