n = int(input())
lst = [['0'], ['1']]
k = 1
for i in range(1, n):
    curr = []
    for j in range(len(lst)-1, -1, -1):
        digit = ['1'] + (['0'] * (k-len(lst[j]))) + lst[j]
        curr.append(digit)
    k += 1
    lst += curr
for num in lst:
    fill = ['0'] * (n-len(num))
    print(''.join(fill+num))
