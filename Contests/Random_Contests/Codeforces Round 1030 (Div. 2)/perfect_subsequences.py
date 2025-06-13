k = int(input())
for _ in range(k):
    lst = input().split()
    print("1" * int(lst[1]) + "0" * (int(lst[0]) - int(lst[1])))

