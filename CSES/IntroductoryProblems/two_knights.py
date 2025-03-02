n = int(input())

for i in range(1, n+1):
    # if i == 1
    squared = i**2
    total = (squared*(squared-1)) >> 1  # Total combinations (n^2)C2
    invalid = (i-1)*(i-2) << 2  # 2 combinations in every 2x3 grid
    valid = total - invalid
    print(valid)
