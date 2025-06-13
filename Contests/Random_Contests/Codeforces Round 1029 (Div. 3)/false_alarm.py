k = int(input())
for _ in range(k):
    n, v = list(map(int, input().split()))
    lst = input().split()
    open = False
    count = v
    for i in range(n):
        if lst[i] == '1' and not open:
            open = True
        if open:
            count -= 1
        if count < 0 and lst[i] == '1':
            print("No")
            break

    else:
        print("Yes")



