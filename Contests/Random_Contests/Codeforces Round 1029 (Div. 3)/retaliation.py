k = int(input())
for _ in range(k):
    n = int(input())
    lst = list(map(int, input().split()))

    y = 2 * lst[0] - lst[1]
    den = n + 1
    if y % den:
        print("No")
    else:
        y = y // den
        x = lst[0] - n * y

        if x < 0 or y < 0:
            print("No")

        else:
            for i in range(n):
                if lst[i] - (x * (i + 1)) - (y * (n - i)) != 0:
                    print("No")
                    break
            else:
                print("Yes")