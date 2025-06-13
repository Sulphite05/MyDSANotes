n = int(input())
for t in range(n):
    y = int(input())
    val = int(round(y**0.5, 0))
    if val and val * val == y:
        print(f'{1} {val-1}')
    elif val == 0:
        print('0 0')
    else:
        print(-1)

